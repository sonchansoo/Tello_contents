#곡선비행을 이용한 클로버모양 비행 => 다양한 모양으로 비행 할 수 있음
# tello 좌표계: +축 기준: x-앞,y-왼,z-위
from djitellopy import Tello
import time

# 텔로 드론 객체 생성
tello = Tello()

# 드론 연결
tello.connect()

# 이륙
tello.takeoff()

tello.move_up(50)  # 50cm 상승

# 곡선이동함수
tello.curve_xyz_speed(0, 100, 0, 100, 0, 0, 30)
time.sleep(2)

tello.curve_xyz_speed(100, 0, 0, 0, -100, 0, 30)
time.sleep(2)

tello.curve_xyz_speed(0, -100, 0, -100, 0, 0, 30)
time.sleep(2)

tello.curve_xyz_speed(-100, 0, 0, 0, 100, 0, 30)
time.sleep(2)

# 원점으로 복귀
tello.go_xyz_speed(0, 0, 0, 30)
# 착륙
tello.land()

# 연결 해제
tello.end()

