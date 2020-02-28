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
from utils import  indx_gen

class puncturer(gr.decim_block):
    """
    docstring for block puncturer
    """
    def __init__(self):
        self.puncture1 = np.array([1,1,0,1,1,0,1,1,0])
        self.puncture2 = np.array([1,0,1,1,0,1,1,0,1])
        self.punc1_inx = indx_gen(len(self.puncture1))
        self.punc2_inx = indx_gen(len(self.puncture2))

        gr.decim_block.__init__(self,
            name="puncturer",
            in_sig=[np.uint8],
            out_sig=[np.uint8], decim=1)


    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        # <+signal processing here+>
        out[:] = in0
        return len(output_items[0])

