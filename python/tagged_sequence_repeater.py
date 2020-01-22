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

class tagged_sequence_repeater(gr.sync_block):
    """
    docstring for block tagged_sequence_repeater
    """
    def __init__(self,sequence):
        # print(sequence)
        self.sequence = sequence
        self.ind = 0
        self.packet_len = len(sequence)
        gr.sync_block.__init__(self,
            name="tagged_sequence_repeater",
            in_sig=None,
            out_sig=[np.complex64])

    def work(self, input_items, output_items):
            out = output_items[0]
            for i in range(0,len(out)):
                if self.ind == self.packet_len: 
                    self.ind = 0
                if self.ind == 0: 
                    self.add_item_tag(0,self.nitems_written(0) + i,pmt.intern("packet_len"),pmt.from_long(self.packet_len))
                out[i] = self.sequence[self.ind]
                self.ind += 1
            return len(out)

