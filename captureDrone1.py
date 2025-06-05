#사진촬영
from djitellopy import Tello
import cv2
from time import sleep
import threading

def capture_images(drone, num_images=300, interval=0.0333):
    """
    드론으로 1초 간격으로 지정된 수의 사진을 캡처하는 함수
    drone: Tello 드론 객체
    num_images: 캡처할 이미지 수
    interval: 이미지 캡처 간격 (초)
    """
    # 드론 카메라 스트리밍 시작
    drone.streamon()

    # 이미지 캡처
    for i in range(num_images):
        # 드론 카메라에서 프레임을 가져옴
        frame = drone.get_frame_read().frame

        # 이미지 저장
        filename = f'tello_image_{i + 1}.jpg'
        cv2.imwrite(filename, frame)
        print(f'file:{filename}')

        # 지정된 간격만큼 대기
        sleep(interval)

    # 드론 카메라 스트리밍 종료
    drone.streamoff()
    

# 드론 객체 생성 및 연결
drone = Tello()
drone.connect()

fps=30 #초당 찍는 사진 개수
interval=1/fps

# 이미지 캡처 함수 호출
stream_thread = threading.Thread(target=capture_images,args=(drone,300,interval))
stream_thread.start()
drone.takeoff()

drone.move_forward(50)
sleep(1)
drone.move_forward(50)
sleep(1)

drone.land()

# 스레드가 종료될 때까지 대기
stream_thread.join()

# 드론 연결 종료
drone.end()

