#!/usr/bin/env
"""
POISE wave rendering example
============================

Usage:
    python test-wav.py test.wav
    
Writes the example waveform to the file test.wav
"""

import sys
from poise import *

# process filename
try:
    filename = sys.argv[1]
except IndexError, ie:
    print "Usage: %s output_filename.wav"%sys.argv[0]
    sys.exit(1)

# concert A sinewave
sfx = osc.sine(440.0, gain=0 )
sfx.next()

# into an ADSR envelope
envsfx = envelope.adsr(sfx,attack=0.2,decay=0.2,sustain=0.4,release=2.0)
envsfx.next()

# save this out at -1dB
wf = WaveFile()
wf.oscillators.append( (envsfx, -1) )
wf.save(filename,200000)
