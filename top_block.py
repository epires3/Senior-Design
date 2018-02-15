#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Thu Feb 15 17:57:54 2018
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

from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from grc_gnuradio import blks2 as grc_blks2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self, samp=4):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")
        _icon_path = "C:\Program Files\GNURadio-3.7\share\icons\hicolor\scalable/apps\gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Parameters
        ##################################################
        self.samp = samp

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32E3

        ##################################################
        # Blocks
        ##################################################
        self.digital_dxpsk_mod_0 = digital.dqpsk_mod(
        	samples_per_symbol=samp,
        	excess_bw=0.35,
        	mod_code="gray",
        	verbose=False,
        	log=False)

        self.digital_dxpsk_demod_0 = digital.dqpsk_demod(
        	samples_per_symbol=samp,
        	excess_bw=0.35,
        	freq_bw=6.28/100.0,
        	phase_bw=6.28/100.0,
        	timing_bw=6.28/100.0,
        	mod_code="gray",
        	verbose=False,
        	log=False
        )
        self.digital_diff_encoder_bb_0 = digital.diff_encoder_bb(2)
        self.digital_diff_decoder_bb_0 = digital.diff_decoder_bb(2)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.blocks_packed_to_unpacked_xx_0 = blocks.packed_to_unpacked_bb(1, gr.GR_MSB_FIRST)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, 'C:\\Users\\ericj\\Senior-Design\\UMass-Dartmouth.png', False)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, 'C:\\Users\\ericj\\Desktop\\out.png', False)
        self.blocks_file_sink_0.set_unbuffered(True)
        self.blks2_packet_encoder_0_0 = grc_blks2.packet_mod_b(grc_blks2.packet_encoder(
        		samples_per_symbol=samp,
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

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blks2_packet_decoder_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blks2_packet_encoder_0_0, 0), (self.blocks_packed_to_unpacked_xx_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_packed_to_unpacked_xx_0, 0), (self.digital_diff_encoder_bb_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blks2_packet_encoder_0_0, 0))
        self.connect((self.digital_diff_decoder_bb_0, 0), (self.blks2_packet_decoder_0, 0))
        self.connect((self.digital_diff_encoder_bb_0, 0), (self.digital_dxpsk_mod_0, 0))
        self.connect((self.digital_dxpsk_demod_0, 0), (self.digital_diff_decoder_bb_0, 0))
        self.connect((self.digital_dxpsk_mod_0, 0), (self.digital_dxpsk_demod_0, 0))

    def get_samp(self):
        return self.samp

    def set_samp(self, samp):
        self.samp = samp

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    return parser


def main(top_block_cls=top_block, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
