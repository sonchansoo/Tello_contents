# 군집비행
from djitellopy import TelloSwarm
from time import sleep

def move_drone(swarm):
        
        swarm.takeoff() 
        sleep(1)
        swarm.move_forward(100)
        sleep(1)
        swarm.move_back(100)
        sleep(1)
        swarm.land()  # 드론 착륙

        
# 여러 대의 드론을 IP 주소로 초기화    
swarm = TelloSwarm.fromIps([
        "192.168.137.4",  # 첫 번째 드론의 IP 주소
        "192.168.137.31"    # 두 번째 드론의 IP 주소
    ])    
    
swarm.connect()
drone1=swarm.tellos[0]
drone2=swarm.tellos[1]

move_drone(swarm)

print(drone1.get_battery)
print(drone2.get_battery)

# 모든 드론과의 연결을 종료
swarm.end()


