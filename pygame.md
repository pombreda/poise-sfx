# Introduction #

Pygame does not support streaming sound generators, so sounds under pygame have to be pre-rendered into a buffer. The method to generate sound from this buffer is via the pygame.sndarray API. If your Sndarray doesn't work, then you cannot create pygame sounds using the library.

Because pygame requires the sound to be rendered into a whole buffer, you cannot use continuous procedural sound, but must limit yourself to one shot samples that won't use up too much RAM. You must take this into consideration when using pygame.