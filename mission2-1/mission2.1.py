from gpiozero import LED, Button
from signal import pause

# 핀 정의
red = LED(20)
yellow = LED(16)
green = LED(7)
blue = LED(8)
button = Button(25, pull_up=True)

def turn_on():
    red.on()
    yellow.on()
    green.on()
    blue.on()
    print("LED ON")

def turn_off():
    red.off()
    yellow.off()
    green.off()
    blue.off()
    print("LED OFF")

# 버튼 눌렀을 때 → ON / 뗐을 때 → OFF
button.when_pressed = turn_on
button.when_released = turn_off

pause()  # 무한 대기
