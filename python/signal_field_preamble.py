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
from utils import SignalField
class signal_field_preamble(gr.sync_block):
    """
    docstring for block signal_field_preamble
    """
    def __init__(self):
        gr.sync_block.__init__(self,
            name="signal_field_preamble",
            in_sig=None,
            out_sig=[np.complex64])
        self.pdus = []
        self.outputs = []
        self.message_port_register_in(pmt.intern("MPDU"))
        self.set_msg_handler(pmt.intern('MPDU'),self.incoming_MPDU)

    def incoming_MPDU(self,mpdu):
        # get the length of the MPDU
        # set a attribute so next time work is called you produce a Signal Field
        if pmt.is_u32vector(mpdu):
            l = len(pmt.u32vector_elements(mpdu))
        self.outputs.append(SignalField(20,6,l))

    def work(self, input_items, output_items):
        out = output_items[0]
        consumed = 0
        # <+signal processing here+>
        for o in range(0,len(out)):
            if len(self.outputs):
                out[o] = self.outputs[0]
                self.outputs.pop(0)
                consumed += 1
        return consumed

