# Introduction #

The pyglet interface to POISE is implemented as a custom pyglet sound `Source`. It behaves just like any other pyglet Source, and streams its mixed audio data.

The `PoiseSource` class can be found in `poise.pyglet`...

```
from poise.pyglet import PoiseSource
```

The `PoiseSource` can be constructed, then used like any other `Source` through a `Player`. Here an instance is queued on a pyglet `Player` and then played.

```
source = PoiseSource()
player = Player()
player.queue(source)
player.play()
```

In this default state, the source will be playing, but having no oscillators, only silence is generated.

To add an oscillator to a source, use the source's `add()` method. Pass in the oscillator generator, and an optional gain level for it to me mixed at.

```
source.add( 
    adsr(
        sine( freq=440.0, gain=-1 ),
        attack=0.1, decay=0.1, sustain=0.0, release=0.0
    ), 
    gain=-6
)
```

If the source is presently playing, the start of this sound will be immediate.

When the generator chain terminates, the oscillator has finished and will be automatically expired from the source. The source will continue to play, and more oscillators can be added. The source is _not_ a queue. If more than one oscillator is added, the two oscillator signals are summed. This is the reason for the gain parameter to add(). This is the mix volume of that osciallator.

If the generator chain never terminates, you will need to keep a handle on the generator to manipulate it.

```
motor = modulate(
    square( freq=82, gain=-3 ),
    square( freq=41, gain=-1 ),
    freq=10
)
source.add( motor, gain=-3 )
```