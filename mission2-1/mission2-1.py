from gpiozero import LEDBoard, Button
from signal import pause

leds = LEDBoard(red=20, yellow=16, green=7, blue=8, pwm=False)
button = Button(25, pull_up=True)

button.when_pressed = leds.on
button.when_released = leds.off

pause()
