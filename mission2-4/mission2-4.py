#!/usr/bin/env python3
from gpiozero import LED, Button
from signal import pause

red = LED(20)      # 빨간 LED (비트 0)
yellow = LED(16)   # 노란 LED (비트 1)
green = LED(7)     # 초록 LED (비트 2)
blue = LED(8)     
button = Button(25, pull_up=True)

# 전역 변수: 카운터 초기값 (0~7)
i = 0

def update_leds():
    global i
    print(f"{i}")
    
    # 비트 0: red LED 제어
    if i & 1:
        red.on()
    else:
        red.off()
    
    # 비트 1: yellow LED 제어
    if (i >> 1) & 1:
        yellow.on()
    else:
        yellow.off()
    
    # 비트 2: green LED 제어
    if (i >> 2) & 1:
        green.on()
    else:
        green.off()
  
    # 카운터 증가: 0~7까지 반복
    i = (i + 1) % 8

# 버튼이 눌리면 update_leds() 함수 호출
button.when_pressed = update_leds

pause()
