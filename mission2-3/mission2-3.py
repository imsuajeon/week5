from gpiozero import LEDBoard, Button
from time import sleep
from signal import pause

# 4개의 LED를 한꺼번에 묶어 leds 객체로 생성
leds = LEDBoard(20, 16, 7, 8)

button = Button(25, pull_up=True)

def domino4():
    for led in leds:
        led.on()
        sleep(1)
        led.off()

button.when_pressed = domino4

pause()
