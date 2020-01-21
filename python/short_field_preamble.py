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

class short_field_preamble(gr.sync_block):
    """
    docstring for block short_field_preamble
    """
    def __init__(self):
        self.preamble = self.create_preamble()
        self.ind = 0
        self.packet_len = len(self.preamble)
        gr.sync_block.__init__(self,
            name="short_field_preamble",
            in_sig=None,
            out_sig=[np.complex64])
            
    def work(self, input_items, output_items):
            out = output_items[0]
            produced = 0
            for i in range(0,len(out)):
                if self.ind == len(self.preamble): self.ind = 0
                if self.ind == 0: self.add_item_tag(0,self.nitems_written(0) + i,pmt.intern("packet_len"),pmt.from_long(self.packet_len))
                out[i] = self.preamble[self.ind]
                self.ind += 1
                produced  += 1
            return produced

    def create_preamble_old(self):
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

    def create_preamble(self):
        symbol = np.zeros(12,dtype=np.complex64)
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
        return symbol

  

  

        

