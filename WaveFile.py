

class WaveFile(object):
    def __init__(self, duration, **kwargs):
        # the presently playing oscilators
        self.oscillators=[]
        
    def set_sample_rate(self,rate):
        return buffers.set_sample_rate(rate)
    
    def save(self, fh, length):
        # save this data to a wave file
        data = self._generate_data(self, length)
    
    def _generate_data(self, samples, offset=0.0):
    
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
            
        return data
        
