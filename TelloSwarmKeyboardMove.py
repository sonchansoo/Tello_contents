#군집+keyboard_control
from djitellopy import TelloSwarm
from time import sleep


swarm = TelloSwarm.fromIps([
    "192.168.137.119",
    "192.168.137.126"
])
swarm.connect()


while True:
    keyboard_control = input("keyboard control activated: ")
    if keyboard_control == "t":
            swarm.takeoff()  
            print(swarm.get_battery())  
            continue
    elif keyboard_control == "l":
            swarm.land()  
            swarm.end()
            print(swarm.get_battery())  
            break
    elif keyboard_control == "w":
            swarm.move_forward(250)   
            continue
    elif keyboard_control == "s":
            swarm.move_back(100)  
            continue
    elif keyboard_control == "a":
            swarm.move_left(30)  
            continue
    elif keyboard_control == "d":
            swarm.move_right(30)  
            continue
    elif keyboard_control == "i":
            swarm.move_up(30)  
            continue
    elif keyboard_control == "o":
            swarm.move_down(20)  
            continue
    else:
            sleep(1)  # 아무 입력도 없을 시 대기
            print(swarm.get_battery())  
            continue

