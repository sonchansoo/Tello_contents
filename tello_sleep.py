from djitellopy import Tello
from time import sleep

# Tello 객체 생성
tello = Tello()

# 드론 연결
tello.connect()

tello.move_forward(100)  # 100cm 앞으로 이동
sleep(1)                 # 1초 동안 대기
tello.move_back(100)     # 100cm 뒤로 이동

# 드론 연결 해제
tello.end()

