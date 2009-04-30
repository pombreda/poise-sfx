

def sine(int offset, int size, np.ndarray buffer, float freq=440.0, float gain=0.0):
    """Return a buffer with a sine wave in it. The buffer is size long and starts at 'offset'
    samples in. The wave has a frequency of 'freq' Hz. 'gain' is the amplitude of the wave with
    0dB being full scale (maximum intensity 1.0)."""
    assert buffer.dtype == DTYPE
    assert buffer.shape[0] >= size
    
    cdef float val=0.0
    cdef int count=0
    while count<size:
        val = sin(float(count+offset)*freq*SAMPLE_TIME)
        buffer[count] = (val * db(gain))
        count += 1
    return buffer
    
def sawtooth(int offset, int size, np.ndarray buffer, float freq=440.0, float gain=0.0):
    """Return a buffer with a sawtooth waveform in it. The render is windowed according to 'offset' and 'size' """
    assert buffer.dtype == DTYPE
    assert buffer.shape[0] >= size
    
    cdef float toffset = offset * SAMPLE_TIME
    cdef float tsize = size * SAMPLE_TIME
    cdef float ti = toffset
    cdef float tend = toffset+tsize
    cdef int i=0
    cdef float val = 0.0
    cdef float div
    cdef int divexp
    cdef float wavelength = 1.0/freq
    for i in range(size):
        # quickly bring back into range 0 - wavelength
        for divexp in range(5,0,-1):
            div = 10 ** divexp
            while ti>wavelength*float(div):
                ti -= wavelength*float(div)
                
        # work out value
        val = ti*2.0/wavelength-1.0
        
        buffer[i] = val * dB(gain)
        
        ti += SAMPLE_TIME
        
    return buffer
    
