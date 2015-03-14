# POISE #

Python Oldskool Ingame Sound Effects

# Overview #

A python extension to create procedural sound effects. Coded for use in gamejams, it support pyglet playback. Uses cython + numpy for rapid buffer generation.

# Requirements #

In order to use POISE you will need

  * python
  * numpy
  * cython (0.11 or better)

Optionally, if you want live sound output, you will need one of the following

  * pyglet
  * pygame

If you have neither of these installed you will be restricted to just rendering Wave files.

# Installation #

First make sure you have numpy and cython and pyglet installed. Then checkout the poise trunk. Build the cython extension by going

```
python setup.py build_ext --inplace
```

This should build the buffer.so importable object. If this stage is correctly completed, you can go `import buffers` from the python shell.

If this statement fails, you may have to tell gcc where some of the header files are. The included makefile is for such a situation on my development Mac, but you shouldn't need it.

Once this is done, to run the test, go

```
python test-pyglet.py
```

# Documentation #

  * [Oscillators](Oscillators.md)
  * [Envelopes](Envelopes.md)
  * [API](API.md)
  * [pyglet](pyglet.md)
  * [pygame](pygame.md)
  * [Writing out wave files](WaveFiles.md)
