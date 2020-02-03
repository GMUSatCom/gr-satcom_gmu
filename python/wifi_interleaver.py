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
import pmt
class wifi_interleaver(gr.decim_block):
    """
    docstring for block wifi_interleaver
    """
    def __init__(self, reverse,ncbps,nbpsc):
        self.first = np.zeros(ncbps,dtype=np.uint8)
        self.second = np.zeros(ncbps,dtype=np.uint8)
        self.ncbps = ncbps
        self.nbpsc = nbpsc
        self.gen_permutations(ncbps, nbpsc)
        gr.decim_block.__init__(self,
            name="wifi_interleaver",
            in_sig=[np.uint8],
            out_sig=[(np.uint8,192)],
            decim=192)
        # self.set_min_output_buffer(192)
    # def forecast(self, noutput_items, ninput_items_required):
    #     #setup size of input_items[i] for work call
    #     for i in range(len(ninput_items_required)):
    #         ninput_items_required[i] = noutput_items + 192

    def gen_permutations(self,ncbps,nbpsc): 
        s = max([1,nbpsc/2])
        for j in range(0,ncbps):
            self.first[j] = s * (j/s) + (j + (16*j)/ncbps) % s

        for i in range(0,ncbps):
            self.second[i] = 16 * i - (ncbps -1) * ((16*i)/ncbps)

    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        # print("=========OUTPUT=========")
        # print("in0 len: {}, out len: {}".format(len(in0),len(out)))
        
        tags = self.get_tags_in_window(0,0,len(in0),pmt.intern("packet_len"))
        for tag in tags:
            key = pmt.to_python(tag.key)
            value = pmt.to_python(tag.value)
            offset = tag.offset
            self.add_item_tag(0,offset,tag.key,pmt.from_long(value/192))
            print("tag: {}, value: {}, offset: {}".format(key,pmt.intern("symbol_num"),offset))

        reverse = False
        assert(len(in0) % self.ncbps == 0)
        symbols = min([len(in0) / self.ncbps])
        for i in range(0,symbols):
            out_vec = np.zeros(self.ncbps,dtype=np.uint8)
            for k in range(0,self.ncbps):
                if reverse:
                    out_vec[self.second[self.first[k]]] = in0[k]
                else:
                    # print("out i: {}, in0 i: {},".format(i * self.ncbps + k,i * self.ncbps + self.second[self.first[k]]))
                    out_vec[k] = in0[int(self.second[self.first[k]])]
            out[i] = out_vec
             
        return len(out)

