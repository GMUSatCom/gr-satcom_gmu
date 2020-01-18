#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Sat Jan  4 20:15:11 2020
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

from PyQt5 import Qt, QtCore
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import satcom_gmu
import sys
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
        self.vec_len = vec_len = 63
        self.short_field_preamble = short_field_preamble = [(0,0), (0,0), (0,0), (0,0), (0, 0), (0, 0), (0, 0), (0, 0), (1.472,1.472j), (0, 0), (0, 0), (0, 0), (-1.472,-1.472j), (0, 0), (0, 0), (0, 0), (1.472,1.472j), (0, 0), (0, 0), (0, 0), (-1.472,-1.472j), (0, 0), (0, 0), (0, 0), (-1.472,-1.472j), (0, 0), (0, 0), (0, 0), (1.472,1.472j), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (-1.472,-1.472j), (0, 0), (0, 0), (0, 0), (-1.472,-1.472j), (0, 0), (0, 0), (0, 0), (1.472,1.472j), (0, 0), (0, 0), (0, 0), (1.472,1.472j), (0, 0), (0, 0), (0, 0), (1.472,1.472j), (0, 0), (0, 0), (0, 0), (1.472,1.472j), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        self.samp_rate = samp_rate = 100e3

        ##################################################
        # Blocks
        ##################################################
        self.satcom_gmu_short_field_preamble_0 = satcom_gmu.short_field_preamble()
        self.blocks_vector_source_x_0 = blocks.vector_source_f((0,0,1,0,0,0,0,0,0,0), False, 1, [])
        self.blocks_stream_to_tagged_stream_0 = blocks.stream_to_tagged_stream(gr.sizeof_float, 1, 2, "packet_len")
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_float*1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_stream_to_tagged_stream_0, 0), (self.satcom_gmu_short_field_preamble_0, 0))
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_stream_to_tagged_stream_0, 0))
        self.connect((self.satcom_gmu_short_field_preamble_0, 0), (self.blocks_null_sink_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_vec_len(self):
        return self.vec_len

    def set_vec_len(self, vec_len):
        self.vec_len = vec_len

    def get_short_field_preamble(self):
        return self.short_field_preamble

    def set_short_field_preamble(self, short_field_preamble):
        self.short_field_preamble = short_field_preamble

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate


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
