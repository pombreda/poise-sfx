import buffers, numpy
from buffers import dB
from buffers import sine as sine_render
from buffers import sawtooth as sawtooth_render
from buffers import square as square_render
from buffers import triangle as triangle_render

BUFFER_START_SIZE = 512

class module(object):
    def __init__(self):
        self.offset = 0             # our present position
        self.buffer = None
        
    def __iter__(self):
        return self
        
    def next(self):
        raise StopIteration
        
    def send(self, length):
        raise StopIteration
        
    def _grow_buffer(self, length):
        """If the buffer size is less than length, allocate a new buffer the size of length. 
        zeros the buffer if it is reallocated"""
        if self.buffer == None or self.buffer.shape[0] < length:
            self.buffer = numpy.zeros( [length], numpy.float )
        
class oscillator(module):
    RENDER_FUNC = None
    
    def __init__(self, freq=440.0, gain=0.0):
        super(oscillator,self).__init__()
        self.freq = freq
        self.gain = gain
        
    def send(self,length):
        # adjust buffer
        o,length = length
        assert isinstance(length, int)
        self._grow_buffer(length)
        self.RENDER_FUNC(self.offset, length, self.buffer, self.freq, self.gain)
        self.offset += length
        return self.buffer
        
class sine(oscillator):
    RENDER_FUNC = sine_render

class sawtooth(oscillator):
    RENDER_FUNC = sawtooth_render

class square(oscillator):
    RENDER_FUNC = square_render

class triangle(oscillator):
    RENDER_FUNC = triangle_render

