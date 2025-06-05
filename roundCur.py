#선회비행 이게 최선
# tello 좌표계: +축 기준: x-앞,y-왼,z-위
from djitellopy import Tello
from time import sleep


# 텔로 드론 객체 생성
tello = Tello()

# 드론 연결
tello.connect()

# 이륙
tello.takeoff()

tello.move_up(50)  # 50cm 상승

# 직선이동함수
tello.go_xyz_speed(0, 90, 0, 30)

# 곡선이동함수
tello.curve_xyz_speed(90, 0, 0, -40, -90, 0, 30)
sleep(2)

tello.go_xyz_speed(0, 30, 0, 30)



# 착륙
tello.land()

# 연결 해제
tello.end()

