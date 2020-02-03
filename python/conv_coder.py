#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2020 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy as np
from gnuradio import gr
from utils import parity, indx_gen
import pmt

class conv_coder(gr.interp_block):
    """
    docstring for block conv_coder
    """
    def __init__(self):
        self.state = np.zeros(7,dtype=np.uint8)
        self.gen1 = np.array([1,0,1,1,0,1,1],dtype=np.uint8)
        self.gen2 = np.array([1,1,1,1,0,0,1],dtype=np.uint8)
        self.puncture1 = np.array([1,1,0,1,1,0,1,1,0])
        self.puncture2 = np.array([1,0,1,1,0,1,1,0,1])
        self.punc1_inx = indx_gen(len(self.puncture1))
        self.punc2_inx = indx_gen(len(self.puncture2))
        gr.interp_block.__init__(self,
            name="conv_coder",
            in_sig=[np.uint8],
            out_sig=[np.uint8], 
            interp=2)
        # self.set_tag_propagation_policy(0) # dont propagate tags
    
    def code_bit(self,bit):
        # print("debug message")
        # print("bit: {}, uint8: {}, type: {}".format(bit,np.uint8(bit),type(bit)))
        assert(bit == 1 or bit == 0)
        assert(type(bit) == type(np.uint8(1)))
        self.state = np.roll(self.state,1)
        self.state[0] = bit 
        bit1 = parity(self.state & self.gen1)
        bit2 = parity(self.state & self.gen2)

        return np.array([bit1,bit2],dtype=np.uint8)
        


    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]

        # tags = self.get_tags_in_window(0,0,len(in0),pmt.intern("packet_len"))
        # for tag in tags:
        #     key = pmt.to_python(tag.key)
        #     value = pmt.to_python(tag.value)
        #     offset = tag.offset
        #     self.add_item_tag(0,offset,tag.key,pmt.from_long(value*2))
        #     print("tag: {}, value: {}, offset: {}".format(key,value,offset))
        assert(not (len(out) % 2))
        out_indx = 0
        for i in range(0,len(in0)):
            bits = self.code_bit(in0[i])
            if self.puncture1[self.punc1_inx.next()]:
                out[out_indx] = bits[0]
                out_indx += 1
            if self.puncture2[self.punc2_inx.next()]:
                out[out_indx] = bits[1]
                out_indx += 1
            

        return out_indx
