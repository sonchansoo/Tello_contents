# 3개의 드론으로 프리스타일 (플립 후 반대 방향으로 이동)
from djitellopy import TelloSwarm
from time import sleep
import threading

def move_drone1(swarm1):
        swarm1.takeoff() 
        sleep(1)
        swarm1.move_up(30)
        sleep(1)
        swarm1.flip_right() 
        sleep(1)
        swarm1.move_left(120)
        sleep(1) 



        swarm1.land()  

def move_drone2(swarm2):
        swarm2.takeoff() 
        sleep(1)
        swarm2.move_up(30)
        sleep(1) 
        swarm2.flip_forward() 
        sleep(1)
        swarm2.move_back(120)
        sleep(1) 

        swarm2.land()  # 드론 착륙

def move_drone3(swarm3):
        swarm3.takeoff() 
        sleep(1)
        swarm3.move_up(30)
        sleep(1) 
        swarm3.flip_left() 
        sleep(1)
        swarm3.move_right(120)
        sleep(1) 

        swarm3.land()  # 드론 착륙

        
        
# 여러 대의 드론을 IP 주소로 초기화    
swarm1 = TelloSwarm.fromIps([
        
        "192.168.137.170"    # 첫 번째 드론의 IP 주소
    ])  

swarm2 = TelloSwarm.fromIps([
   
        "192.168.137.160"    # 두 번째 드론의 IP 주소
    ])  


swarm3 = TelloSwarm.fromIps([
    
        "192.168.137.21"    # 세 번째 드론의 IP 주소
    ])  

 
 
swarm1.connect()
swarm2.connect()
swarm3.connect()

move_thread1 = threading.Thread(target=move_drone1, args=(swarm1,))
move_thread1.start()

move_thread2 = threading.Thread(target=move_drone2, args=(swarm2,))
move_thread2.start()

move_thread3 = threading.Thread(target=move_drone3, args=(swarm3,))
move_thread3.start()

move_thread1.join()  
move_thread2.join()
move_thread3.join()     

# 모든 드론과의 연결을 종료
swarm1.end()
swarm2.end()
swarm3.end()







