from gpiozero import LEDBoard, Button
from signal import pause

# 3개의 LED를 한 번에 묶어 leds 객체로 생성
leds = LEDBoard(20, 16, 7)  # 순서대로 red, yellow, green
button = Button(25, pull_up=True)

i = 0  

def counter():
    global i
    print(i)
    leds.value = [(i >> bit) & 1 for bit in range(3)] 
    i = (i + 1) % 8

button.when_pressed = counter
pause()
