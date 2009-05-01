"""

POISE
=====
Python Oldskool Ingame Sound Effects

Support library. Quickly calculates buffers. manipulates buffers. 
"""

cdef int NUM_SINE_VALUES = 8192
cdef np.ndarray SINE_TABLE = np.zeros([NUM_SINE_VALUES, 1], dtype=DTYPE)

def fill_sine():
    cdef int x
    cdef float theta
    for x in range(NUM_SINE_VALUES):
        theta = float(x)*2.*math.pi/(float(NUM_SINE_VALUES))
        SINE_TABLE[x] = math.sin(theta)

# run on import to fill table
fill_sine()

# calculate sin by looking up the closest value
def sin(float theta):
    cdef float x = theta*float(NUM_SINE_VALUES)/(2.*math.pi) + 2.0 * math.pi / float(NUM_SINE_VALUES)
    cdef float answer = SINE_TABLE[int(x)%NUM_SINE_VALUES]
    return answer
    
def sin_true(float theta):
    cdef float answer = math.sin(theta)
    return answer
    
def cos(float theta):
    return sin(theta+math.pi/4.0)

# turn decibel into a multiplier
def dB(float gain=0.0):
    cdef float db = 10.0 ** ( gain / 20.0 )
    return db



