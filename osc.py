import buffers, numpy
from buffers import dB
from buffers import sine as sine_render
from buffers import sawtooth as sawtooth_render
from buffers import square as square_render
from buffers import triangle as triangle_render

BUFFER_START_SIZE = 256*1024

def sine(freq=440.0,gain=0.0):
    buffer = numpy.zeros([BUFFER_START_SIZE], numpy.float)
    (offset,size) = yield buffer
    
    while True:
        buffer = sine_render(offset, size, buffer, freq, gain)
        (offset, size) = yield buffer
        

def sawtooth(freq=440.0, gain=0.0):
    buffer = numpy.zeros([BUFFER_START_SIZE], numpy.float)
    (offset,size) = yield buffer
    
    while True:
        buffer = sawtooth_render(offset, size, buffer, freq, gain)
        (offset, size) = yield buffer

def square(freq=440.0, gain=0.0):
    buffer = numpy.zeros([BUFFER_START_SIZE], numpy.float)
    (offset,size) = yield buffer
    
    while True:
        buffer = square_render(offset, size, buffer, freq, gain)
        (offset, size) = yield buffer

def triangle(freq=440.0, gain=0.0):
    buffer = numpy.zeros([BUFFER_START_SIZE], numpy.float)
    (offset,size) = yield buffer
    
    while True:
        buffer = triangle_render(offset, size, buffer, freq, gain)
        (offset, size) = yield buffer


