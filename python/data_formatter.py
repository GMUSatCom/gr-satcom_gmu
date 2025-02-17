#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2020 SATCOM GMU
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
import math
from gnuradio import gr
import pmt
from bitarray import bitarray
from utils import indx_gen
class data_formatter(gr.sync_block):
    """
    docstring for block data_formatter
    """
    def __init__(self,ofdm_params):
        self.ofdm_params = ofdm_params
        self.buffer = np.array([],dtype=np.uint8)
        self.packet_len = None
        self.insert_tag = False
        self.n_sym = 0
        self.n_data = 0
        self.n_pad = 0
        self.offset = long(0)
        gr.sync_block.__init__(self,
            name="data_formatter",
            in_sig=None,
            out_sig=[np.uint8])
        self.message_port_register_in(pmt.intern("MPDU"))
        self.set_msg_handler(pmt.intern('MPDU'),self.incoming_MPDU)

    def incoming_MPDU(self,mpdu):
        assert(pmt.is_u8vector(mpdu))
        data = np.array(pmt.u8vector_elements(mpdu),dtype=np.uint8)
        data_len = len(data) * 8
        n_sym = math.ceil((16 + 6 + data_len) / (self.ofdm_params.ndbps * 1.0))
        n_data = n_sym * self.ofdm_params.ndbps
        n_pad = n_data - (16 + data_len)

        assert(not (n_pad % 8))
        # print("n_pad: {}".format(n_pad))
        scrambler_initiation = np.array([0,0],dtype=np.uint8)
        data = np.concatenate((scrambler_initiation,data,np.zeros(int(n_pad/8),dtype=np.uint8)))
        # print("n_data: {},dataLen: {},data: {}".format(n_data,data.size,data))

        self.buffer = np.append(self.buffer,data)

        self.packet_len = long(len(self.buffer))
        # print("packet_len: {}".format(self.packet_len))
        self.insert_tag = True



    def work(self, input_items, output_items):
        out = output_items[0]
        produced = long(0)
        
        # print(self.insert_tag)
        # print(self.offset)
        for o in range(0,len(out)):
            if self.insert_tag:
                self.add_item_tag(0,self.offset + long(o),pmt.intern("packet_len"),pmt.from_long(self.packet_len))
                # print("a tag was inserted into the stream. offset: {}".format(self.offset))
                self.insert_tag = False 

            if len(self.buffer) > 0:
                out[o] = self.buffer[0]
                self.buffer = self.buffer[1:]
                produced += 1
        self.offset += produced
        return produced
