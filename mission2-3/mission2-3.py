from gpiozero import LED, Button
from time import sleep
from signal import pause

# 핀 정의
red = LED(20)
yellow = LED(16)
green = LED(7)
blue = LED(8)
button = Button(25, pull_up=True)

def sequence_leds():
    # 빨간 LED on / off
    red.on()
    sleep(1)
    red.off()

    # 노란 LED on / off
    yellow.on()
    sleep(1)
    yellow.off()

    # 초록 LED on / off
    green.on()
    sleep(1)
    green.off()

    # 파란 LED on / off
    blue.on()
    sleep(1)
    blue.off()

# 버튼 눌림 시 sequence_leds 함수 호출
button.when_pressed = sequence_leds

pause() 
