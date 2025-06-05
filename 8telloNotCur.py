#8자비행 +곡선X
from djitellopy import Tello
from time import sleep

# 텔로 드론 객체 생성
tello = Tello()

# 드론 연결
tello.connect()

# 이륙
tello.takeoff() # 기본 120cm 상승

# 선회 비행 (시계 방향으로 360도 회전)
for _ in range(12):  # 30도씩 12번 회전하여 360도 회전
    tello.rotate_clockwise(30)
    tello.move_forward(35)
     
sleep(1)
# 선회 비행 (반시계 방향으로 360도 회전)
for _ in range(12):  # 30도씩 12번 회전하여 360도 회전
    tello.rotate_counter_clockwise(30)
    tello.move_forward(35)
    

# 착륙
tello.land()

# 연결 해제
tello.end()

