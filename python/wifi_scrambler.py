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
from utils import scrambler
from bitarray import bitarray
from utils import indx_gen
class wifi_scrambler(gr.sync_block):
    """
    docstring for block wifi_scrambler
    """
    def __init__(self,seed):
        self.state = np.array([np.uint8(i) for i in seed])
        # self.state = np.ones(7,dtype=np.uint8)
        self.sequence = self.generate_sequence()
        self.seq_cnt = indx_gen(len(self.sequence))
        gr.sync_block.__init__(self,
            name="wifi_scrambler",
            in_sig=[np.uint8],
            out_sig=[np.uint8])


    def scramble(self,bit):
        feedback = self.state[3] ^ self.state[6]
        output = bit ^ feedback
        self.state = np.roll(self.state,1)
        self.state[0] = feedback
        return feedback ^ bit

    # def scramble(self,inpt):
    #     output = np.zeros((8,),dtype=np.uint8)
    #     inpt = np.unpackbits([inpt])
    #     for i,val in enumerate(inpt):
    #         feedback = self.state[6] ^ self.state[3]
    #         output[i] = (val ^ feedback)
    #         self.state = np.roll(self.state,1)
    #         self.state[0] = feedback 
    #     # print(hex(np.packbits(output)[0]))
    #     print(output)

        # return np.packbits(output)
    def generate_sequence(self):
        inpt = np.zeros(127,dtype=np.uint8)
        outpt = np.zeros(127,dtype=np.uint8)
        for i,val in enumerate(inpt):
            outpt[i] = self.scramble(val) 
        
        # print(outpt)
        return outpt

    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        self.generate_sequence()
        for i in range(0,len(out)):
            if i >= len(in0): break
            out[i] = in0[i] ^ self.sequence[self.seq_cnt.next()]
        return len(output_items[0])

