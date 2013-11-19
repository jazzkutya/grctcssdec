#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Tue Nov 19 23:21:43 2013
##################################################

from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import numbersink2
from grc_gnuradio import wxgui as grc_wxgui
from math import pi
from optparse import OptionParser
import wx

class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 44100

        ##################################################
        # Blocks
        ##################################################
        self.wxgui_numbersink2_0 = numbersink2.number_sink_f(
        	self.GetWin(),
        	unit="Hz",
        	minval=50,
        	maxval=280,
        	factor=1,
        	decimal_places=2,
        	ref_level=0,
        	sample_rate=samp_rate,
        	number_rate=15,
        	average=False,
        	avg_alpha=None,
        	label="Number Plot",
        	peak_hold=False,
        	show_gauge=True,
        )
        self.Add(self.wxgui_numbersink2_0.win)
        self.blocks_moving_average_xx_0 = blocks.moving_average_ff(samp_rate/50, 25/pi, 200)
        self.blocks_keep_one_in_n_0 = blocks.keep_one_in_n(gr.sizeof_float*1, 10)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.band_pass_filter_0 = filter.fir_filter_ccc(1, firdes.complex_band_pass(
        	1, samp_rate, 60, 255, 100, firdes.WIN_BLACKMAN, 6.76))
        self.audio_source_0 = audio.source(samp_rate, "default", True)
        self.analog_pll_freqdet_cf_0 = analog.pll_freqdet_cf(200*2.0*pi/samp_rate, 260*2.0*pi/samp_rate, 60*2.0*pi/samp_rate)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_moving_average_xx_0, 0), (self.wxgui_numbersink2_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.band_pass_filter_0, 0))
        self.connect((self.band_pass_filter_0, 0), (self.analog_pll_freqdet_cf_0, 0))
        self.connect((self.audio_source_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.analog_pll_freqdet_cf_0, 0), (self.blocks_keep_one_in_n_0, 0))
        self.connect((self.blocks_keep_one_in_n_0, 0), (self.blocks_moving_average_xx_0, 0))


# QT sink close method reimplementation

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.band_pass_filter_0.set_taps(firdes.complex_band_pass(1, self.samp_rate, 60, 255, 100, firdes.WIN_BLACKMAN, 6.76))
        self.analog_pll_freqdet_cf_0.set_loop_bandwidth(200*2.0*pi/self.samp_rate)
        self.analog_pll_freqdet_cf_0.set_max_freq(260*2.0*pi/self.samp_rate)
        self.analog_pll_freqdet_cf_0.set_min_freq(60*2.0*pi/self.samp_rate)
        self.blocks_moving_average_xx_0.set_length_and_scale(self.samp_rate/50, 25/pi)

if __name__ == '__main__':
    import ctypes
    import os
    if os.name == 'posix':
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = top_block()
    tb.Start(True)
    tb.Wait()

