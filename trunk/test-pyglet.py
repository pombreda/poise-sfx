from poise import *
from pyglet.media import Player

player = Player()
poise = PoiseSource(999999999)
player.queue(poise)
player.play()

sfx = osc.sine(500.0, gain=0 )
envsfx = envelope.adsr(sfx,attack=0.2,decay=0.2,sustain=0.2,release=2.0)
poise.oscillators.append( (envsfx, -1) )

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
