import buffers, numpy
from buffers import dB
from buffers import sine as sine_render_c

BUFFER_START_SIZE = 256*1024

def adsr(gen, attack=0.4, decay=0.8, sustain=2.0, release=2.5, again=0.0, sgain=-6.0, noisefloor=-96.0 ):
    offset,size = yield
    while True:
        buffer = gen.send((offset,size))
        buffer = buffers.adsr(offset,size,buffer,attack,decay,sustain,release,again,sgain,noisefloor)
        offset, size = yield buffer
            
