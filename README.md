grctcssdec
==========

CTCSS decoder with gnuradio

very early stage, only a flowchart yet but it's usable with a CTCSS frequency chart (try wikipedia).

Minimal docs here

Most cpu hungry part is the complex bandpass filter which seems needed
by the pll block to lock on the ctcss frequency accurately.
The pll is also disturbed by DC which proved to be pretty heavy with linrad nbfm.
I've loosened up the settings already to eat less cpu (most important is the transition width).
I need to refresh my memory (actually re-study :)) about the windowing stuff.

The pll block needs about this much sample rate for signals in the range 60-270Hz because
it has a limited bandwidth (max pi/50 in radian/samples).

The keep 1 in N block also help reduce cpu load, no need to do moving average at full sample rate.
