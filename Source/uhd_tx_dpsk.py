#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: UHD TX DPSK
# Generated: Thu Feb 15 18:28:34 2018
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from grc_gnuradio import blks2 as grc_blks2
from optparse import OptionParser
import sip
import sys
from gnuradio import qtgui


class uhd_tx_dpsk(gr.top_block, Qt.QWidget):

    def __init__(self, address='addr=192.168.10.4', freq=2.45e9, gain=0, samp_rate=32e3):
        gr.top_block.__init__(self, "UHD TX DPSK")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("UHD TX DPSK")
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

        self.settings = Qt.QSettings("GNU Radio", "uhd_tx_dpsk")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Parameters
        ##################################################
        self.address = address
        self.freq = freq
        self.gain = gain
        self.samp_rate = samp_rate

        ##################################################
        # Variables
        ##################################################
        self.tun_gain = tun_gain = 0
        self.tun_freq = tun_freq = 2.45e9
        self.samps_per_sym = samps_per_sym = 4
        self.ampl = ampl = 0.7

        ##################################################
        # Blocks
        ##################################################
        self._tun_gain_range = Range(0, 20, 1, 0, 200)
        self._tun_gain_win = RangeWidget(self._tun_gain_range, self.set_tun_gain, 'UHD Tx Gain', "counter_slider", float)
        self.top_layout.addWidget(self._tun_gain_win)
        self._tun_freq_range = Range(2.4e9, 2.5e9, 1, 2.45e9, 200)
        self._tun_freq_win = RangeWidget(self._tun_freq_range, self.set_tun_freq, 'UHD Freq (Hz)', "counter_slider", float)
        self.top_layout.addWidget(self._tun_freq_win)
        self.qtgui_number_sink_0 = qtgui.number_sink(
            gr.sizeof_char,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1
        )
        self.qtgui_number_sink_0.set_update_time(0.10)
        self.qtgui_number_sink_0.set_title("")

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        units = ['', '', '', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0.set_min(i, 0)
            self.qtgui_number_sink_0.set_max(i, 1)
            self.qtgui_number_sink_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0.set_label(i, labels[i])
            self.qtgui_number_sink_0.set_unit(i, units[i])
            self.qtgui_number_sink_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0.enable_autoscale(True)
        self._qtgui_number_sink_0_win = sip.wrapinstance(self.qtgui_number_sink_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_0_win)
        self.digital_dxpsk_mod_0 = digital.dqpsk_mod(
        	samples_per_symbol=samps_per_sym,
        	excess_bw=0.35,
        	mod_code="gray",
        	verbose=False,
        	log=False)

        self.digital_dxpsk_demod_0 = digital.dqpsk_demod(
        	samples_per_symbol=samps_per_sym,
        	excess_bw=0.35,
        	freq_bw=6.28/100.0,
        	phase_bw=6.28/100.0,
        	timing_bw=6.28/100.0,
        	mod_code="gray",
        	verbose=False,
        	log=False
        )
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, 'C:\\Users\\ericj\\Senior-Design\\Source\\test_image.png', False)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, 'C:\\Users\\ericj\\Desktop\\out.jpeg', False)
        self.blocks_file_sink_0.set_unbuffered(True)
        self.blks2_packet_encoder_0 = grc_blks2.packet_mod_b(grc_blks2.packet_encoder(
        		samples_per_symbol=samps_per_sym,
        		bits_per_symbol=2,
        		preamble='',
        		access_code='',
        		pad_for_usrp=True,
        	),
        	payload_length=8,
        )
        self.blks2_packet_decoder_0 = grc_blks2.packet_demod_b(grc_blks2.packet_decoder(
        		access_code='',
        		threshold=-1,
        		callback=lambda ok, payload: self.blks2_packet_decoder_0.recv_pkt(ok, payload),
        	),
        )
        self._ampl_range = Range(0, 1, 0.01, 0.7, 200)
        self._ampl_win = RangeWidget(self._ampl_range, self.set_ampl, 'Amplitude', "counter_slider", float)
        self.top_layout.addWidget(self._ampl_win)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blks2_packet_decoder_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blks2_packet_decoder_0, 0), (self.qtgui_number_sink_0, 0))
        self.connect((self.blks2_packet_encoder_0, 0), (self.digital_dxpsk_mod_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blks2_packet_encoder_0, 0))
        self.connect((self.digital_dxpsk_demod_0, 0), (self.blks2_packet_decoder_0, 0))
        self.connect((self.digital_dxpsk_mod_0, 0), (self.digital_dxpsk_demod_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "uhd_tx_dpsk")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_tun_gain(self):
        return self.tun_gain

    def set_tun_gain(self, tun_gain):
        self.tun_gain = tun_gain

    def get_tun_freq(self):
        return self.tun_freq

    def set_tun_freq(self, tun_freq):
        self.tun_freq = tun_freq

    def get_samps_per_sym(self):
        return self.samps_per_sym

    def set_samps_per_sym(self, samps_per_sym):
        self.samps_per_sym = samps_per_sym

    def get_ampl(self):
        return self.ampl

    def set_ampl(self, ampl):
        self.ampl = ampl


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "-a", "--address", dest="address", type="string", default='addr=192.168.10.4',
        help="Set IP Address [default=%default]")
    parser.add_option(
        "-f", "--freq", dest="freq", type="eng_float", default=eng_notation.num_to_str(2.45e9),
        help="Set Default Frequency [default=%default]")
    parser.add_option(
        "-g", "--gain", dest="gain", type="eng_float", default=eng_notation.num_to_str(0),
        help="Set Default Gain [default=%default]")
    parser.add_option(
        "-s", "--samp-rate", dest="samp_rate", type="complex", default=32e3,
        help="Set Sample Rate [default=%default]")
    return parser


def main(top_block_cls=uhd_tx_dpsk, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(address=options.address, freq=options.freq, gain=options.gain, samp_rate=options.samp_rate)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
