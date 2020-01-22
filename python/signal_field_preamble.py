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
from utils import SignalField,convolutional_encoder,interleaver,puncturer
class signal_field_preamble(gr.sync_block):
    """
    docstring for block signal_field_preamble
    """
    def __init__(self):
        gr.sync_block.__init__(self,
            name="signal_field_preamble",
            in_sig=None,
            out_sig=[np.uint8])
        self.pdus = []
        self.outputs = []
        self.packet_cnt = 0
        self.packet_len = 48
        self.message_port_register_in(pmt.intern("MPDU"))
        self.set_msg_handler(pmt.intern('MPDU'),self.incoming_MPDU)

    def incoming_MPDU(self,mpdu):
        # get the length of the MPDU
        # set a attribute so next time work is called you produce a Signal Field
        if pmt.is_u32vector(mpdu):
            l = len(pmt.u32vector_elements(mpdu))
            s = SignalField(20,36,l)
            s = self.prepare_signal(s.encode())
            self.outputs.extend(s)


    def prepare_signal(self,bit_arr):
        # print("signal raw, len: {}".format(len(bit_arr)))
        # print(bit_arr)
        output = convolutional_encoder(bit_arr)
        # print("convolution, len: {}".format(len(output)))
        # print(output)
        output = interleaver(output,False,48,2)
        # print("interleaving".format(len(output)))
        # print(output)
        return output

    def work(self, input_items, output_items):
        out = output_items[0]
        produced = 0
        if self.nitems_written(0) == 0:
            self.add_item_tag(0,0,pmt.intern("packet_len"),pmt.from_long(self.packet_len))
        for o in range(0,len(out)):
            if len(self.outputs) > 0:
                if self.packet_cnt == self.packet_len:
                    self.packet_cnt = 0
                    self.add_item_tag(0,self.nitems_written(0) + o,pmt.intern("packet_len"),pmt.from_long(self.packet_len))
                out[o] = np.uint8(self.outputs[0])
                self.outputs.pop(0)
                produced += 1
                self.packet_cnt += 1
        return produced

