from gpiozero import LEDBoard, Button
from signal import pause

leds = LEDBoard(red=20, yellow=16, green=7, blue=8)
button = Button(25, pull_up=True)

# 버튼을 누를 때마다 LEDs 전체를 토글
button.when_pressed = leds.toggle

pause()
