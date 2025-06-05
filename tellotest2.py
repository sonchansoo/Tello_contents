# 두 개의 드론으로 자유비행
from djitellopy import TelloSwarm
from time import sleep
import threading

def move_drone1(swarm1):
        
        swarm1.takeoff() 
        sleep(1)
        swarm1.move_up(50) 
        sleep(1)
        swarm1.move_forward(30)
        sleep(1)
        swarm1.flip_right() 
        sleep(2)  
        sleep(2) 
        swarm1.land()  # 드론 착륙

def move_drone2(swarm2):
        swarm2.takeoff() 
        sleep(1)
        swarm2.move_up(50) 
        sleep(1)
        swarm2.move_back(30)
        sleep(1)
        swarm2.flip_left() 
        sleep(2)  
        swarm2.move_left() 
        sleep(1) 
        swarm2.flip_left() 
        sleep(2) 
        swarm2.land()  # 드론 착륙

        
# 여러 대의 드론을 IP 주소로 초기화    
swarm1 = TelloSwarm.fromIps([
        "192.168.137.160"  # 첫 번째 드론의 IP 주소
          
    ])  

swarm2 = TelloSwarm.fromIps([
     
        "192.168.137.21"    # 두 번째 드론의 IP 주소
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