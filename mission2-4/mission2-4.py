from gpiozero import LEDBoard, Button
from signal import pause

leds = LEDBoard(20, 16, 7, 8)
button = Button(25, pull_up=True)

i = 0  

def counter():
    global i
    print(i)
    leds.value = [(i >> bit) & 1 for bit in range(4)] 
    i = (i + 1) % 16

button.when_pressed = counter
pause()
