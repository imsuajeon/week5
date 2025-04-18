from gpiozero import LED, Button
from signal import pause

# 핀 정의
red = LED(20)
yellow = LED(16)
green = LED(7)
blue = LED(8)
button = Button(25, pull_up=True)

# LED 상태 변수 (True: LED가 켜짐, False: LED가 꺼짐)
led_on = False

def toggle():
    global led_on
    if led_on:
        red.off()
        yellow.off()
        green.off()
        blue.off()
        print("LED OFF")
        led_on = False
    else:
        red.on()
        yellow.on()
        green.on()
        blue.on()
        print("LED ON")
        led_on = True

# 버튼 눌림 시 토글 함수 호출
button.when_pressed = toggle

pause()  # 프로그램이 종료되지 않고 무한 대기
