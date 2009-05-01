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


import numpy, sysimport pygletpyglet.options['audio'] = ('openal', 'silent')
from pyglet.media.procedural import ProceduralSourceimport ctypes, math

BUFFER_START_SIZE=56000

import buffers
from buffers import dB

def sine(freq=440.0,gain=0.0):
    buffer = numpy.zeros([BUFFER_START_SIZE], numpy.float)
    (offset,size) = yield buffer
    
    while True:
        buffer = buffers.sine(offset, size, buffer, freq, gain)
        (offset, size) = yield buffer
        
def adsr(gen, attack=0.1, decay=0.1, sustain=1.0, release=0.5, again=0.0, sgain=0.0, noisefloor=-96.0 ):
    offset,size = yield
    for buffer in gen:
        buffer = buffers.adsr(offset,size,buffer,attack,decay,sustain,release,again,sgain,noisefloor)
        offset, size = yield buffer
        gen.send(offset,size)
class PoiseSource(ProceduralSource):    def __init__(self, duration, **kwargs):        super(PoiseSource,self).__init__(duration, **kwargs)                # the presently playing oscilators        self.oscillators=[]        
        # set the cython extension rendering rate to this pyglet rate        buffers.set_sample_rate(self.sample_rate)            @property    def sample_rate(self):        return self.audio_format.sample_rate            def _generate_data(self, bytes, offset):        #print bytes,offset        if self._bytes_per_sample == 1:            samples = bytes            data = (ctypes.c_ubyte * bytes)()                        bias = 127            amplitude = 127        else:               samples = bytes >> 1            data = (ctypes.c_short * (bytes>>1))()                    bias = 0            amplitude = 32767        
        results = []
        finished_list = []
        for osc, intensity in self.oscillators:
            # feed into the generator the next section parameters
            try:
                # render a buffer through the generator chain
                #print "2"
                buff = osc.send( (offset,samples) )
                #print "buf=",buff
            except StopIteration, si:
                finished_list.append( (osc,intensity) )
                # todo: zero buffer[(osc,intensity)]
                
            # ajdust buffer with gain
            # buff = buffers.gain( offset, samples, buff, gain=intensity )
            
            # make a list of oscilator 'tracks' to be mixed
            results.append(buff)
        
        FLOAT_MAX = 1.0
        if len(results):
            buffer = sum(results)
            #print buffer
            # fill in our samples            for i in range(samples):
                value = buffer[i]                s=((value/FLOAT_MAX)*float(amplitude) + float(bias))                                data[i] = int(s)
                #print data[i],",",                # remove finished oscillators                for osc,intensity in finished_list:                    self.oscillators.remove((osc,intensity))                
            print data[0]
                        # return the buffer        return data
        
        
if __name__=="__main__":
    from pyglet.media import Player    player = Player()    poise = PoiseSource(999999999)    player.queue(poise)    player.play()    sfx = sine(5200)
    sfx.next()    poise.oscillators.append( (sfx, dB(-12)) )    from pyglet import app    from pyglet import window    from pyglet import text    win = window.Window()    label = text.Label('tesing pyglet playback',                              font_name='Times New Roman',                              font_size=24,                              x=win.width//2, y=win.height//2,                              anchor_x='center', anchor_y='center')    @win.event    def on_draw():        win.clear()        label.draw()    from pyglet.window import key    #@win.event    #def on_key_press(symbol, modifiers):    #    if symbol == key._1:    #        poise.oscillators.append( (keysfx['1'](), dB(-12)) )    #    elif symbol == key._2:    #           poise.oscillators.append( (keysfx['2'](), dB(-12)) )    app.run()
