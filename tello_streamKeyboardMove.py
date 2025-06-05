#영상스트리밍 + keyboard
from djitellopy import Tello
import cv2
from time import sleep
import threading

def stream_video(drone):
    drone.streamon() 
    frame_reader = drone.get_frame_read()  # 프레임 리더 객체를 가져옴
    width,height=960,720

    while True:
        frame = frame_reader.frame  # 드론으로부터 프레임을 가져옴
        if frame is not None:
            frame = cv2.resize(frame, (width, height))  # 프레임 크기를 조정
            cv2.imshow("Drone Stream", frame)  # 드론의 영상을 창에 표시
           

        if cv2.waitKey(1) & 0xFF == ord('x'):  # 'x' 키를 누르면 스트리밍을 종료
            break

    drone.streamoff()  
    print(f"stream off")


drone = Tello()
drone.connect()  


stream_thread = threading.Thread(target=stream_video, args=(drone,))
stream_thread.start()

while True:
    keyboard_control = input("keyboard control activated: ")
    if keyboard_control == "t":
            drone.takeoff() 
            continue
    elif keyboard_control == "l":
            drone.land() 
            break
    elif keyboard_control == "w":
            drone.move_forward(50) 
            continue
    elif keyboard_control == "s":
            drone.move_back(50)  
            continue
    elif keyboard_control == "a":
            drone.move_left(50)  
            continue
    elif keyboard_control == "d":
            drone.move_right(50)  
            continue
    elif keyboard_control == "i":
            drone.move_up(50)  
            continue
    elif keyboard_control == "o":
            drone.move_down(50)   
            continue
    elif keyboard_control == "q":
            drone.rotate_counter_clockwise(50)  
            continue
    elif keyboard_control == "e":
            drone.rotate_clockwise(50)   
            continue
    else:
            sleep(1)
            continue
    
# 스레드가 종료될 때까지 기다림
stream_thread.join() 
drone.end()
# 프로그램 종료 시 모든 OpenCV 창을 닫음
cv2.destroyAllWindows()




