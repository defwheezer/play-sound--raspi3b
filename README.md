# play-sound--raspi3b
Play sound files on Raspberry Pi 3b

Part of animatronic projects that use sound to trigger to activate servo, etc.
When a Raspberry Pi 3b is needed to generate realistic Text-To-Speech (tts),
the Pi will also be used to play sound files.

Simpler projects should use a sound module like (Adafruit Audio FX Sound Board) for playing sounds.

A 'Comimark KA2284 Audio Power Level Indicator Module' is used to get sound level.

An Arduino (5v Vcc) is used to read the (5v) LEDs on the Level Indicator Module (directly solder jumper wires from LEDs to Arduino GIOP)
