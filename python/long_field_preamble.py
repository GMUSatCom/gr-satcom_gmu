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

class long_field_preamble(gr.sync_block):
    """
    docstring for block long_field_preamble
    """
    def __init__(self, repeat=False):
        self.repeat = repeat
        self.did = False
        self.preamble = self.create_preamble()
        gr.sync_block.__init__(self,
            name="long_field_preamble",
            in_sig=None,
            out_sig=[(np.complex64,162)])

    def create_preamble(self):
        #FIX Pad to a power of 2
        symbol = np.array([0,0,0,0,0,0,1, 1,-1,-1,1,1,-1,1,-1,1,1,1,1, 1, 1, -1, -1, 1, 1, -1, 1, -1, 1, 1, 1, 1, 0,1, -1, -1, 1, 1, -1, 1, -1, 1, -1, -1, -1, -1, -1, 1, 1, -1, -1, 1, -1, 1, -1, 1, 1, 1, 1,0,0,0,0,0],dtype=np.complex64)
        symbol = np.fft.fftshift(symbol)
        ifft = np.fft.ifft(symbol,n=64)
        time_domain = np.concatenate((ifft[32:],ifft,ifft,ifft[0:2]))#change the 2 to a 1 to remove the padding
        time_domain[0] = time_domain[0]/2
        time_domain[160] = time_domain[160]/2
        time_domain[161] = 0 # The vector length must be divisible by 2 so the last value is padding
        return time_domain

    def work(self, input_items, output_items):
        out = output_items[0]
        out[0] = self.preamble
        if self.did == False or self.repeat:
            self.did = True
            return 1
        else:
            return -1

