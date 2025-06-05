#영상스트리밍 후 동영상 저장 및 파일열기 +keyboard
from djitellopy import Tello
import cv2
from time import sleep
import threading
import subprocess

def stream_video_and_record(drone, output_video):
    drone.streamon()  # 드론의 영상 스트리밍을 킴
    frame_reader = drone.get_frame_read()  # 프레임 리더 객체를 가져옴
    
    height, width = 720, 960
    video_writer = cv2.VideoWriter(output_video, cv2.VideoWriter_fourcc(*'mp4v'), 30, (width, height))

    while True:
        frame = frame_reader.frame  # 드론으로부터 프레임을 가져옴
        if frame is not None:
            frame = cv2.resize(frame, (width, height))  # 프레임 크기를 조정
            cv2.imshow("Drone Stream", frame)  # 드론의 영상을 창에 표시
            video_writer.write(frame)  # 프레임을 비디오 파일에 기록

        if cv2.waitKey(1) & 0xFF == ord('q'):  # 'q' 키를 누르면 스트리밍을 종료
            break

    video_writer.release()  # 비디오 파일 저장 객체를 해제
    drone.streamoff()  # 드론의 영상 스트리밍을 끔
    print(f"Video saved to {output_video}")


drone = Tello()
drone.connect()  # 드론에 연결함

output_video = 'tello_flight_video1.mp4'  # 생성될 동영상 파일 이름
stream_thread = threading.Thread(target=stream_video_and_record, args=(drone, output_video))
stream_thread.start()

while True:
    keyboard_control = input("keyboard control activated: ")
    if keyboard_control == "t":
            drone.takeoff()  # 드론을 이륙시킴
            print(drone.get_battery())
            continue
    elif keyboard_control == "l":
            drone.land()  # 드론을 착륙시킴
            print(drone.get_battery())
            break
    elif keyboard_control == "w":
            drone.move_forward(10)  # 드론을 앞으로 이동
            print(drone.get_battery())
            continue
    elif keyboard_control == "s":
            drone.move_back(10)  # 드론을 뒤로 이동
            print(drone.get_battery())
            continue
    elif keyboard_control == "a":
            drone.move_left(10)  # 드론을 왼쪽으로 이동
            print(drone.get_battery())
            continue
    elif keyboard_control == "d":
            drone.move_right(10)  # 드론을 오른쪽으로 이동
            continue
    elif keyboard_control == "i":
            drone.move_up(10)  # 드론을 위로 이동
            print(drone.get_battery())
            continue
    elif keyboard_control == "o":
            drone.move_down(10)  # 드론을 아래로 이동
            print(drone.get_battery())
            continue
    else:
            sleep(1)
            print(drone.get_battery())
            continue

    # 스레드가 종료될 때까지 기다림
stream_thread.join()

    # 드론 연결 종료
drone.end()

    # 프로그램 종료 시 모든 OpenCV 창을 닫음
cv2.destroyAllWindows()

    # 동영상 경로 및 열기
file_path = r'C:\Users\son\Desktop\Drone_github\tello_flight_video1.mp4'
subprocess.run(['start', file_path], shell=True)


