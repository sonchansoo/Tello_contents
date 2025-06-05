# 영상스트리밍 
from djitellopy import Tello
import cv2
import threading
from time import sleep

def stream_video(drone):
    drone.streamon()  
    frame_reader = drone.get_frame_read()  # 프레임 리더 객체를 가져옴
    width,height=960,720

    while True:
        frame = frame_reader.frame  # 드론으로부터 프레임을 가져옴
        if frame is not None:
            frame = cv2.resize(frame, (width, height))  # 프레임 크기를 조정
            cv2.imshow("Drone Stream", frame)  # 드론의 영상을 창에 표시
           

        if cv2.waitKey(1) & 0xFF == ord('q'):  # 'q' 키를 누르면 스트리밍을 종료
            break

    drone.streamoff()  
    print(f"stream off")


drone = Tello()
drone.connect()

# 스레드 인스턴스 생성 시 args는 튜플로 전달해야 함
stream_thread = threading.Thread(target=stream_video, args=(drone,))
stream_thread.start()

# 스트리밍 켜는 시간동안 움직임을 지연시키기 위함
sleep(3)

drone.takeoff() 
print("Takeoff complete")
        
drone.move_forward(100)
        
drone.land()
print("Landing complete")

# 스레드가 종료될 때까지 기다림
stream_thread.join()

drone.end()

# 프로그램 종료 시 모든 OpenCV 창을 닫음
cv2.destroyAllWindows()

