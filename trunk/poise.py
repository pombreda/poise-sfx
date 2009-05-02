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
import buffers
import osc
import envelope

BUFFER_START_SIZE = 256*1024
FLOAT_MAX = 1.0

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
        
