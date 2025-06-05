# 군집비행 4개 군무
from djitellopy import TelloSwarm
from time import sleep
import threading

def move_drone1(swarm1):
        
        swarm1.takeoff() 
        sleep(1)
        swarm1.move_up(50)
        sleep(1)
        swarm1.move_down(50)
        sleep(1)
        swarm1.land()  # 드론 착륙

def move_drone2(swarm2):
        
        swarm2.takeoff() 
        sleep(1)
        swarm2.move_down(50)
        sleep(1)
        swarm2.move_up(50)
        sleep(1)
        swarm2.land()  # 드론 착륙

        
# 여러 대의 드론을 IP 주소로 초기화    
swarm1 = TelloSwarm.fromIps([
        "192.168.137.4",  # 첫 번째 드론의 IP 주소
        "192.168.137.31"    # 두 번째 드론의 IP 주소
    ])  

swarm2 = TelloSwarm.fromIps([
        "192.168.137.4",  # 첫 번째 드론의 IP 주소
        "192.168.137.31"    # 두 번째 드론의 IP 주소
    ])  
    
swarm1.connect()
swarm2.connect()

move_thread1 = threading.Thread(target=move_drone1, args=(swarm1,))
move_thread1.start()

move_thread2 = threading.Thread(target=move_drone2, args=(swarm2,))
move_thread2.start()

move_thread1.join()  
move_thread2.join()  

# 모든 드론과의 연결을 종료
swarm1.end()
swarm2.end()


