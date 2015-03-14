# POISE envelopes

# Envelopes #

## adsr ##

```
from poise.envelopes import adsr
gen = adsr( source, attack, decay, sustain, release, again, sgain, noisefloor )
```

### def adsr (source, attack=0.4, decay=0.8, sustain=2.0, release=2.5, again=0.0, sgain=-6.0, noisefloor=-96.0) ###
source : source osciallator/generator

attack : attack time in seconds. Time to rise from noisefloor to attack gain.

decay : decay time in seconds. Time it takes to decay from attack gain to sustain gain.

sustain : how long in seconds to sustain at the sustain gain level

release : how long in seconds to fall back into the noise floor.

again : attack gain. peak level of attack. in decibels.

sgain : sustain gain. level of sustain in decibels.

noisefloor : the decibel level of 'silence'. default is good for most uses.