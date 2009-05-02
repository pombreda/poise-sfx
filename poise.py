"""

POISE
=====
Python Oldskool Ingame Sound Effects

Support library. Quickly calculates buffers. manipulates buffers. 

This cython extension renders and manipulates data in numpy arrays in a very fast way.

use like:

>>> import poise
>>> 
"""


import numpy, sys

import pyglet
pyglet.options['audio'] = ('openal', 'silent')

from pyglet.media.procedural import ProceduralSource, AudioData
import ctypes, math

BUFFER_START_SIZE = 256*1024
FLOAT_MAX = 1.0

import buffers
from buffers import dB
from buffers import sine as sine_render_c

# for profiling
def sine_render(o,s,b,f,g):
    return sine_render_c(o,s,b,f,g)

def sine(freq=440.0,gain=0.0):
    buffer = numpy.zeros([BUFFER_START_SIZE], numpy.float)
    (offset,size) = yield buffer
    
    while True:
        buffer = sine_render(offset, size, buffer, freq, gain)
        (offset, size) = yield buffer

def adsr(gen, attack=0.4, decay=0.8, sustain=2.0, release=2.5, again=0.0, sgain=-6.0, noisefloor=-96.0 ):
    offset,size = yield
    while True:
        buffer = gen.send((offset,size))
        buffer = buffers.adsr(offset,size,buffer,attack,decay,sustain,release,again,sgain,noisefloor)
        offset, size = yield buffer
            
class PoiseSource(ProceduralSource):
    def __init__(self, duration, **kwargs):
        super(PoiseSource,self).__init__(duration, **kwargs)
        
        # the presently playing oscilators
        self.oscillators=[]
        
        # set the cython extension rendering rate to this pyglet rate
        buffers.set_sample_rate(self.sample_rate)
        
    @property
    def sample_rate(self):
        return self.audio_format.sample_rate
    
    def _get_audio_data(self, bytes):
        bytes = min(bytes, self._max_offset - self._offset)
        if bytes <= 0:
            return None
            
        # make our buffers word aligned
        if bytes%2:
            bytes+=1
        
        timestamp = float(self._offset) / self._bytes_per_second
        duration = float(bytes) / self._bytes_per_second
        data = self._generate_data(bytes, self._offset)
        self._offset += bytes
        is_eos = self._offset >= self._max_offset

        return AudioData(data,
                         bytes,
                         timestamp,
                         duration)
    
    def _generate_data(self, bytes, offset):
        #print bytes, offset
        if self._bytes_per_sample == 1:
            samples = bytes
            data = (ctypes.c_ubyte * bytes)()
            
            bias = 127
            amplitude = 127
        else:   
            # divide it all by two to make it into samples
            samples = bytes >> 1
            offset = offset >> 1
            data = (ctypes.c_short * samples)()
        
            bias = 0    
            amplitude = 32767
        
        store = numpy.zeros([samples], numpy.float)
        for osc,intensity in self.oscillators:
            buff = osc.send( (offset,samples) )
            
            # adjust gain on buffer
            buff = buffers.gain( offset, samples, buff, gain=intensity )
    
            # accumulate
            store += buff[:samples]
    
        FLOAT_MAX = 1.0
        for i in range(samples):
            value = store[i]
            s=((value/FLOAT_MAX)*float(amplitude) + float(bias))
                
            data[i] = int(s)
            #print data[i],",",
            # remove finished oscillators
            
        return data
        #return data    
        
