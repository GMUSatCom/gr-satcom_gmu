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
class wifi_scrambler(gr.sync_block):
    """
    docstring for block wifi_scrambler
    """
    def __init__(self,seed):
        self.state = bitarray(seed)
        gr.sync_block.__init__(self,
            name="wifi_scrambler",
            in_sig=[np.uint8],
            out_sig=[np.uint8])

    def scramble(self,inpt):
        output = bitarray('')
        inpt = bitarray(inpt)
        for i in inpt:
            feedback = self.state[6] ^ self.state[3]
            output.append(i ^ feedback)
            self.state.insert(0,feedback)
            self.state.pop()
        return output

    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        for i in range(0,len(out)):
            out[i] = self.scramble(in0[i])
        return len(output_items[0])

