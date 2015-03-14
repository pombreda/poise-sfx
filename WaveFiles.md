# Writing WAV Files #

Here is how you write wav sample files out of your sound effects. Instead of queuing your oscillators on a source, you create a WaveFile instance, queue them on that, then save out the file. For example:

```
from poise import *

# build the sound effect generator
sfx = osc.sine(440.0, gain=0 )
envsfx = envelope.adsr(sfx,attack=0.2,decay=0.2,sustain=0.4,release=2.0)

# write the wave to "test.wav", with length of 200,000 samples
wf = WaveFile()
wf.add( envsfx, -1 )
wf.save("test.wav",200000)
```