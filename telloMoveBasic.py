from djitellopy import Tello

# Tello 객체 생성
tello = Tello()

# 드론 연결
tello.connect()

# 이륙
tello.takeoff()

# 명령어 수행 
tello.move_up(30)       # 30cm 위로 이동
tello.move_down(30)     # 30cm 아래로 이동
tello.move_left(30)     # 30cm 왼쪽으로 이동
tello.move_right(30)    # 30cm 오른쪽으로 이동
tello.move_forward(30) # 30cm 앞으로 이동
tello.move_back(30)    # 30cm 뒤로 이동
tello.rotate_clockwise(90)        # 시계 방향으로 90도 회전
tello.rotate_counter_clockwise(90) # 반시계 방향으로 90도 회전

tello.flip_forward()    # 앞쪽으로 플립 (공중제비)
tello.flip_back()       # 뒤쪽으로 플립
tello.flip_left()       # 왼쪽으로 플립
tello.flip_right()      # 오른쪽으로 플립


# 착륙
tello.land()

# 드론 연결 해제
tello.end()
