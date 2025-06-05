from djitellopy import Tello
import cv2
from time import sleep
import threading
import subprocess
import os

def stream_video_and_record(drone, output_video):
    drone.streamon()  
    frame_reader = drone.get_frame_read()  # 프레임 리더 객체를 가져옴
    
    height, width = 720, 960
    fps = 30  # Tello 드론의 기본 프레임 속도
    video_writer = cv2.VideoWriter(output_video, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    while True:
        frame = frame_reader.frame  # 드론으로부터 프레임을 가져옴
        if frame is not None:
            frame = cv2.resize(frame, (width, height))  # 프레임 크기를 조정
            cv2.imshow("Drone Stream", frame)  # 드론의 영상을 창에 표시
            video_writer.write(frame)  # 프레임을 비디오 파일에 기록

        if cv2.waitKey(1) & 0xFF == ord('q'):  # 'q' 키를 누르면 스트리밍을 종료
            break

    video_writer.release()  # 비디오 파일 저장 객체를 해제
    drone.streamoff()  
    print(f"Video saved to {output_video}")

def move_drone(drone):
    sleep(1)
    drone.takeoff()
    drone.move_forward(90)
    drone.land()

# 드론 객체 생성 및 연결
drone = Tello()
drone.connect()

# 비디오 저장 경로 및 파일 이름
save_dir = r'C:\Users\son\Desktop\tello1'
output_video = os.path.join(save_dir, 'tello_flight_video1.mp4')

# 비디오 저장 경로가 존재하지 않으면 생성
if not os.path.exists(save_dir):
    os.makedirs(save_dir)
    

# 드론 이동 스레드 시작
move_thread = threading.Thread(target=move_drone, args=(drone,))
move_thread.start()

# 스트리밍 및 녹화 스레드 시작
stream_thread = threading.Thread(target=stream_video_and_record, args=(drone, output_video))
stream_thread.start()

# 스레드가 종료될 때까지 기다림
move_thread.join()
stream_thread.join()

drone.end()
cv2.destroyAllWindows()

# 동영상 열기
file_path= r'C:\Users\son\Desktop\tello1\tello_flight_video1.mp4'
subprocess.run(['start', file_path], shell=True)

