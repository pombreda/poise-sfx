import buffers, numpy
from buffers import dB
from buffers import sine as sine_render_c

BUFFER_START_SIZE = 256*1024

# for profiling
def sine_render(o,s,b,f,g):
    return sine_render_c(o,s,b,f,g)

def sine(freq=440.0,gain=0.0):
    buffer = numpy.zeros([BUFFER_START_SIZE], numpy.float)
    (offset,size) = yield buffer
    
    while True:
        buffer = sine_render(offset, size, buffer, freq, gain)
        (offset, size) = yield buffer
