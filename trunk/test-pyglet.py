from poise import *
from pyglet.media import Player

player = Player()
poise = PoiseSource(999999999)
player.queue(poise)
player.play()

sfx = osc.sine(440.0, gain=0 )
sfx.next()
envsfx = envelope.adsr(sfx,attack=0.2,decay=0.2,sustain=0.4,release=2.0)
envsfx.next()
#poise.oscillators.append( (envsfx, -6) )

#sfx = envsfx

# render 1 second of 440 Hz sine
#buffer = sfx.send( (0,48000) )
##o=[]
#for i in buffer[:48000/440]:
#    o.append(float(int(i*500)+500)/10)
    
#print ",".join([str(a) for a in o])

from poise import WaveFile

wf = WaveFile()
wf.oscillators.append( (envsfx, -1) )
wf.save("test.wav",200000)

    
import sys
sys.exit()


from pyglet import app
from pyglet import window

from pyglet import text

win = window.Window()

label = text.Label('testing pyglet playback',
                          font_name='Times New Roman',
                          font_size=24,
                          x=win.width//2, y=win.height//2,
                          anchor_x='center', anchor_y='center')

@win.event
def on_draw():
    win.clear()
    label.draw()

from pyglet.window import key

app.run()
