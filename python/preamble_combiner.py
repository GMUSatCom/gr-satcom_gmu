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
class preamble_combiner(gr.interp_block):
    """
    docstring for block preamble_combiner
    """
    def __init__(self):
        gr.interp_block.__init__(self,
            name="preamble_combiner",
            in_sig=[(np.complex64,64),(np.complex64,64),(np.complex64,64)],
            out_sig=[np.complex64],
            interp=160+160+80+1)

        # Dont propagate tags
        self.set_tag_propagation_policy(0)
    def window(self,inpt,func):
        inpt = np.array(inpt)
        return np.multiply(inpt,np.array(func))

    def periodic_extend(self,inpt, extension_len):
        assert(extension_len > len(inpt))
        output = np.array([],dtype=np.complex64)
        for a in range(0,extension_len/len(inpt)):
            output = np.append(output,inpt)

        output = np.append(output,output[:extension_len % len(inpt)])
        return output

    def cyclic_extend(self,inpt,extension_len):
        return np.append(inpt[len(inpt)-extension_len:],inpt)

    def work(self, input_items, output_items):
        # there has to be a better way to write this function. do that later
        s = input_items[0][0]
        l = input_items[1][0]
        sig = input_items[2][0]

        wndw = [1] * 161
        wndw[0] = 0.5
        wndw[160] = 0.5

        sig_wndw = [1] * 81
        sig_wndw[0] = 0.5
        sig_wndw[80] = 0.5

        # SHORT FIELD
        s = self.periodic_extend(s,161)
        s = self.window(s,wndw)

        # LONG FIELD
        l = self.periodic_extend(l,len(l) * 2)
        end_val = l[0]
        l = self.cyclic_extend(l,len(l)/4)
        l = np.append(l,[end_val])
        l = self.window(l,wndw)

        # SIGNAL FIELD
        end_val = sig[0]
        sig = self.cyclic_extend(sig,len(sig)/4)
        sig = np.append(sig,[end_val])
        sig = self.window(sig,sig_wndw)

        # COMBINING PARTS
        combined = np.array([],dtype=np.complex64)
        combined = np.append(combined,s[:-1])
        combined = np.append(combined, [s[-1] + l[0]])
        combined = np.append(combined,l[1:-1])
        combined = np.append(combined, [l[-1] + sig[0]])
        combined = np.append(combined,sig[1:])

        self.add_item_tag(0,self.nitems_written(0) + 1,pmt.intern("packet_len"),pmt.from_long(len(combined)))
        out = output_items[0]
        out[:] = combined
        return len(output_items[0])

