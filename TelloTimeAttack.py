from djitellopy import Tello
from time import sleep
import time

tello = Tello()
tello.connect()

while True:
    keyboard_control = input("keyboard control activated: ")
    if keyboard_control == "t":
            start_time = time.perf_counter()
            tello.takeoff()  # 드론 이륙
            continue   
    elif keyboard_control == "l":
            tello.land()  # 드론 착륙
            end_time = time.perf_counter()
            tello.end()   # 착륙 시 연결종료
            elapsed_time = end_time - start_time
            print(f'time:{elapsed_time}')
            break
    elif keyboard_control == "w":
            tello.move_forward(50)  # 드론 앞으로 이동
            continue
    elif keyboard_control == "s":
            tello.move_back(50)  # 드론 뒤로 이동
            continue
    elif keyboard_control == "a":
            tello.move_left(50)  # 드론 왼쪽으로 이동
            continue
    elif keyboard_control == "d":
            tello.move_right(50)  # 드론 오른쪽으로 이동
            continue
    elif keyboard_control == "i":
            tello.move_up(50)  # 드론 고도 상승
            continue
    elif keyboard_control == "o":
            tello.move_down(50)  # 드론 고도 하강
            continue
    else:
            sleep(1)  # 아무 입력도 없을 시 대기
            continue


