# 4개의 드론으로 프리스타일
from djitellopy import TelloSwarm
from time import sleep
import threading

def move_drone1(swarm1):
        swarm1.takeoff() 
        sleep(1)
        swarm1.move_forward(50)
        sleep(1)
        swarm1.rotate_clockwise(720) 
        sleep(1)
        swarm1.flip_forward() 
        sleep(1)

        swarm1.land()  

def move_drone2(swarm2):
        swarm2.takeoff() 
        sleep(1)
        swarm2.move_forward(50)
        sleep(1)
        swarm2.rotate_clockwise(720) 
        sleep(1)
        swarm2.flip_forward() 
        sleep(1)

        swarm1.land()  

def move_drone3(swarm3):
        swarm3.takeoff() 
        sleep(1)
        swarm3.move_forward(50)
        sleep(1)
        swarm3.rotate_clockwise(720) 
        sleep(1)
        swarm3.flip_forward() 
        sleep(1)

        swarm1.land()  

def move_drone4(swarm4):
        swarm4.takeoff() 
        sleep(1)
        swarm4.move_forward(50)
        sleep(1)
        swarm4.rotate_clockwise(720) 
        sleep(1)
        swarm4.flip_forward() 
        sleep(1)

        swarm1.land() 
        
# 여러 대의 드론을 IP 주소로 초기화    
swarm1 = TelloSwarm.fromIps([
        
        "192.168.137.170"    # 첫 번째 드론의 IP 주소
    ])  

swarm2 = TelloSwarm.fromIps([
   
        "192.168.137.113"    # 두 번째 드론의 IP 주소
    ])  


swarm3 = TelloSwarm.fromIps([
    
        "192.168.137.21"    # 세 번째 드론의 IP 주소
    ])  

swarm4 = TelloSwarm.fromIps([
    
        "192.168.137.160"    # 세 번째 드론의 IP 주소
    ])    
 
swarm1.connect()
swarm2.connect()
swarm3.connect()
swarm4.connect()

move_thread1 = threading.Thread(target=move_drone1, args=(swarm1,))
move_thread1.start()

move_thread2 = threading.Thread(target=move_drone2, args=(swarm2,))
move_thread2.start()

move_thread3 = threading.Thread(target=move_drone3, args=(swarm3,))
move_thread3.start()

move_thread4 = threading.Thread(target=move_drone4, args=(swarm4,))
move_thread4.start()

move_thread1.join()  
move_thread2.join()
move_thread3.join()    
move_thread4.join()    

# 모든 드론과의 연결을 종료
swarm1.end()
swarm2.end()
swarm3.end()
swarm4.end()

