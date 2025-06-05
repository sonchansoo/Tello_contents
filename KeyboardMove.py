#keyboard_control
from djitellopy import Tello
from time import sleep



drone = Tello()
drone.connect()


while True:
    keyboard_control = input("keyboard control activated: ")
    if keyboard_control == "t":
            drone.takeoff()  # 드론 이륙
            print(drone.get_battery())  
            continue
    elif keyboard_control == "l":
            drone.land()  # 드론 착륙
            drone.end()   # 착륙 시 연결종료
            print(drone.get_battery())  
            break
    elif keyboard_control == "w":
            drone.move_forward(250)  # 드론 앞으로 이동
            print(drone.get_battery())  
            continue
    elif keyboard_control == "s":
            drone.move_back(100)  # 드론 뒤로 이동
            print(drone.get_battery())  
            continue
    elif keyboard_control == "a":
            drone.move_left(30)  # 드론 왼쪽으로 이동
            print(drone.get_battery())  
            continue
    elif keyboard_control == "d":
            drone.move_right(30)  # 드론 오른쪽으로 이동
            print(drone.get_battery())  
            continue
    elif keyboard_control == "i":
            drone.move_up(30)  # 드론 고도 상승
            print(drone.get_battery())  
            continue
    elif keyboard_control == "o":
            drone.move_down(20)  # 드론 고도 하강
            print(drone.get_battery())  
            continue
    else:
            sleep(1)  # 아무 입력도 없을 시 대기
            print(drone.get_battery())  
            continue


