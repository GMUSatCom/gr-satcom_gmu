#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Wed Feb 26 01:04:09 2020
##################################################

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

def struct(data): return type('Struct', (object,), data)()
from PyQt5 import Qt
from PyQt5 import Qt, QtCore
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import fec
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from ofdm_wifi_preamble import ofdm_wifi_preamble  # grc-generated hier_block
from optparse import OptionParser
import numpy as np
import pmt
import satcom_gmu
import sip
from gnuradio import qtgui


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")

        if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
            self.restoreGeometry(self.settings.value("geometry").toByteArray())
        else:
            self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))

        ##################################################
        # Variables
        ##################################################
        self.fft_len = fft_len = 64
        self.vec_len = vec_len = 63
        self.variable_constellation_rect_0 = variable_constellation_rect_0 = digital.constellation_rect(([-1-1j, -1+1j, 1+1j, 1-1j]), ([0, 1, 3, 2]), 4, 2, 2, 1, 1).base()
        self.short_field_preamble = short_field_preamble = [(0,0), (0,0), (0,0), (0,0), (0, 0), (0, 0), (0, 0), (0, 0), (1.472,1.472j), (0, 0), (0, 0), (0, 0), (-1.472,-1.472j), (0, 0), (0, 0), (0, 0), (1.472,1.472j), (0, 0), (0, 0), (0, 0), (-1.472,-1.472j), (0, 0), (0, 0), (0, 0), (-1.472,-1.472j), (0, 0), (0, 0), (0, 0), (1.472,1.472j), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (-1.472,-1.472j), (0, 0), (0, 0), (0, 0), (-1.472,-1.472j), (0, 0), (0, 0), (0, 0), (1.472,1.472j), (0, 0), (0, 0), (0, 0), (1.472,1.472j), (0, 0), (0, 0), (0, 0), (1.472,1.472j), (0, 0), (0, 0), (0, 0), (1.472,1.472j), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        self.short_field_obj = short_field_obj = struct({'sequence': np.array([1,-1,1,-1,-1,1,-1,-1,1,1,1,1] ,dtype=np.complex64) * complex(1,1) * 1.472, 'subcarriers': ([-24,-20,-16,-12,-8,-4,4,8,12,16,20,24],), 'periodicExtendTo': 161, })
        self.samp_rate = samp_rate = 32e3
        self.ofdm_params = ofdm_params = struct({'bandwidth': 20, 'dataRate': 6, 'ncbpsc': 4, 'ncbps': 192, 'ndbps': 144, 'rate': 3.0/4.0, 'rateCode': 'idk', 'modulationType': "16qam", })
        self.long_field_obj = long_field_obj = struct({'sequence': np.array([1, 1,-1,-1,1,1,-1,1,-1,1,1,1,1, 1, 1, -1, -1, 1, 1, -1, 1, -1, 1, 1, 1, 1, 1, -1, -1, 1, 1, -1, 1, -1, 1, -1, -1, -1, -1, -1, 1, 1, -1, -1, 1, -1, 1, -1, 1, 1, 1, 1],dtype=np.complex64), 'subcarriers': (range(-26,0) + range(1,27),), 'cyclicPrefixLen': fft_len/4, 'periodicExtendTo': 161, })
        self.fft_len_0 = fft_len_0 = 64


        self.conv_wifi_coder = conv_wifi_coder = fec.cc_encoder_make(864, 7, 2, ([0133,0171]), 0, fec.CC_STREAMING, False)


        self.constellation = constellation = digital.constellation_16qam().base()

        self.a1 = a1 = satcom_gmu.utils.OFDM_Params()

        ##################################################
        # Blocks
        ##################################################
        self.satcom_gmu_wifi_scrambler_0 = satcom_gmu.wifi_scrambler("1011101")
        self.satcom_gmu_data_formatter_0 = satcom_gmu.data_formatter(ofdm_params)
        self.satcom_gmu_conv_coder_0 = satcom_gmu.conv_coder()
        self.qtgui_time_sink_x_0 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(2):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.ofdm_wifi_preamble_0 = ofdm_wifi_preamble()
        self.blocks_tag_debug_0 = blocks.tag_debug(gr.sizeof_char*1, 'Packet Length', "packet_len"); self.blocks_tag_debug_0.set_display(True)
        self.blocks_repack_bits_bb_0 = blocks.repack_bits_bb(8, 1, "", False, gr.GR_LSB_FIRST)
        self.blocks_null_sink_2 = blocks.null_sink(gr.sizeof_char*1)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_message_strobe_0 = blocks.message_strobe(a1.vec_test(), 5000)

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_message_strobe_0, 'strobe'), (self.ofdm_wifi_preamble_0, 'data_in'))
        self.msg_connect((self.blocks_message_strobe_0, 'strobe'), (self.satcom_gmu_data_formatter_0, 'MPDU'))
        self.connect((self.blocks_repack_bits_bb_0, 0), (self.satcom_gmu_wifi_scrambler_0, 0))
        self.connect((self.ofdm_wifi_preamble_0, 0), (self.blocks_null_sink_0, 0))
        self.connect((self.ofdm_wifi_preamble_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.satcom_gmu_conv_coder_0, 0), (self.blocks_null_sink_2, 0))
        self.connect((self.satcom_gmu_conv_coder_0, 0), (self.blocks_tag_debug_0, 0))
        self.connect((self.satcom_gmu_data_formatter_0, 0), (self.blocks_repack_bits_bb_0, 0))
        self.connect((self.satcom_gmu_wifi_scrambler_0, 0), (self.satcom_gmu_conv_coder_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_fft_len(self):
        return self.fft_len

    def set_fft_len(self, fft_len):
        self.fft_len = fft_len

    def get_vec_len(self):
        return self.vec_len

    def set_vec_len(self, vec_len):
        self.vec_len = vec_len

    def get_variable_constellation_rect_0(self):
        return self.variable_constellation_rect_0

    def set_variable_constellation_rect_0(self, variable_constellation_rect_0):
        self.variable_constellation_rect_0 = variable_constellation_rect_0

    def get_short_field_preamble(self):
        return self.short_field_preamble

    def set_short_field_preamble(self, short_field_preamble):
        self.short_field_preamble = short_field_preamble

    def get_short_field_obj(self):
        return self.short_field_obj

    def set_short_field_obj(self, short_field_obj):
        self.short_field_obj = short_field_obj

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)

    def get_ofdm_params(self):
        return self.ofdm_params

    def set_ofdm_params(self, ofdm_params):
        self.ofdm_params = ofdm_params

    def get_long_field_obj(self):
        return self.long_field_obj

    def set_long_field_obj(self, long_field_obj):
        self.long_field_obj = long_field_obj

    def get_fft_len_0(self):
        return self.fft_len_0

    def set_fft_len_0(self, fft_len_0):
        self.fft_len_0 = fft_len_0

    def get_conv_wifi_coder(self):
        return self.conv_wifi_coder

    def set_conv_wifi_coder(self, conv_wifi_coder):
        self.conv_wifi_coder = conv_wifi_coder

    def get_constellation(self):
        return self.constellation

    def set_constellation(self, constellation):
        self.constellation = constellation

    def get_a1(self):
        return self.a1

    def set_a1(self, a1):
        self.a1 = a1


def main(top_block_cls=top_block, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
