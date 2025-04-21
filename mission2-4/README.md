#### 미션 2-4 : 버튼이 눌릴 때마다 4-bit 카운터 값 증가시키기
---
#### 미션 2-4 해결사 수아의 유튭: https://youtu.be/0LWyPa03CkE?si=7rP4xP1azdQw4t5H
---
#### 회로
![image](https://github.com/user-attachments/assets/942d67be-aac1-4577-99a2-63ebb42da008)
---
#### 코드 원리
LEDBoard 클래스를 사용해 LED를 leds라는 객채로 만들고 counter 함수를 만들어서 i의 하위 3비트를 이용하여 각 led를 끄고 키며 i를 0~7까지 순환키고 버튼 콜백에 바인딩함.

