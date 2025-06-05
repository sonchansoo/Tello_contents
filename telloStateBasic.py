from djitellopy import Tello

# Tello 객체 생성
tello = Tello()

# 드론 연결
tello.connect()

# 배터리 상태 확인
battery_level = tello.get_battery()
print(f"Battery level: {battery_level}%")

# 속도를 10cm/s로 설정 (기본값: 10, 범위: 10-100)
tello.set_speed(10) 

# 드론의 온도 확인
temperature = tello.get_temperature()  

# 현재 고도 확인
height = tello.get_height()  

# 비행 시간 확인
flight_time = tello.get_flight_time()  

# 드론 연결 해제
tello.end()
