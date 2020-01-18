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
from gnuradio import gr,blocks

class short_field_preamble(gr.sync_block):
    """
    docstring for block short_field_preamble
    """
    def __init__(self,repeat = False):
        self.preamble = self.create_preamble()
        self.loc = 0
        self.did = False
        self.repeat = repeat
        gr.sync_block.__init__(self,
            name="short_field_preamble",
            in_sig=None,
            out_sig=[(np.complex64,162)])

    def create_preamble(self):
        symbol = np.zeros(64,dtype=np.complex64)
        symbol[-24+32]=complex(1,1)
        symbol[-16+32]=complex(1,1)
        symbol[-4+32]=complex(1,1)
        symbol[12+32]=complex(1,1)
        symbol[16+32]=complex(1,1)
        symbol[20+32]=complex(1,1)
        symbol[24+32]=complex(1,1)
        symbol[-20+32]=complex(-1,-1)
        symbol[-12+32]=complex(-1,-1)
        symbol[-8+32]=complex(-1,-1)
        symbol[4+32]=complex(-1,-1)
        symbol[8+32]=complex(-1,-1)
        symbol = symbol * 1.472 # This is sqrt(13/6) in other places in the documentation
        symbol = np.fft.fftshift(symbol)
        ifft = np.fft.ifft(symbol,n=64)
        time_domain = np.concatenate((ifft,ifft,ifft[:34]))
        time_domain[0] = time_domain[0]/2
        time_domain[160] = time_domain[160]/2
        time_domain[161] = 0 # The vector length must be divisible by 2 so the last value is padding
        return time_domain

    def split_preamble(self, outn):
        # note used when outputting a vector
        loc = self.loc
        if outn >= len(self.preamble) - loc or outn >= len(self.preamble):
            advance = len(self.preamble) - loc 
        else:
            advance = outn
        output = self.preamble[loc:loc+advance]
        self.loc = loc + advance
        return (output, len(output))

    def work(self, input_items, output_items):
        out = output_items[0]
        out[0] = self.preamble
        if self.did == False or self.repeat:
            self.did = True
            return 1
        else:
            return -1

