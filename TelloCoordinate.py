from djitellopy import Tello

# Tello 객체 생성
tello = Tello()

# 드론 연결
tello.connect()

tello.takeoff()

# 두 좌표 사이에 경로를 곡선이동
tello.curve_xyz_speed(0, 100, 0, 100, 0, 0, 30)


tello.land()
 
# 드론 연결 해제
tello.end()

