# Oscillators #

The POISE oscillators are imported from poise.osc

```
from poise.osc import sine, square, triangle, sawtooth
```

Each is a python generator that will generate buffers.

## sine ##

```
from poise.osc import sine
gen = sine( freq, gain )
```

generates a sine wave

frequency is in hertz. gain is in decibels.

## square ##

```
from poise.osc import square
gen = square( freq, gain )
```

generates a square wave

## sawtooth ##

```
from poise.osc import sawtooth
gen = sawtooth( freq, gain )
```

generates a sawtooth wave

## triangle ##

```
from poise.osc import triangle
gen = triangle(freq,gain)
```

generates a triangular waveform

## silence ##

```
from poise.osc import silence
gen = silence()
```

generates zeros. completely silent.

## noise ##

```
from poise.osc import noise
gen = noise(gain)
```

generates white noise.

gain is the waveforms instantaneous peak maximum level. Just straight random noise scaled to that gain.