#1.75배속
from djitellopy import Tello
import cv2
from time import sleep
import threading
import subprocess

def stream_video_and_record(drone, output_video):
    drone.streamon()  
    frame_reader = drone.get_frame_read()  # 프레임 리더 객체를 가져옴
    
    height, width = 720, 960
    fps = 30  #Tello 드론의 기본 프레임
    video_writer = cv2.VideoWriter(output_video, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    while True:
        frame = frame_reader.frame  # 드론으로부터 프레임을 가져옴
        if frame is not None:
            frame = cv2.resize(frame, (width, height))  # 프레임 크기를 조정
            cv2.imshow("Drone Stream", frame)  # 드론의 영상을 창에 표시
            video_writer.write(frame)  # 프레임을 비디오 파일에 기록

        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break

    video_writer.release()  # 비디오 파일 저장 객체를 해제
    drone.streamoff() 

def speed_up_video(input_video, output_video, speed_factor):
    # 비디오 파일을 읽어옴
    cap = cv2.VideoCapture(input_video)
    fps = cap.get(cv2.CAP_PROP_FPS)
    new_fps = fps * speed_factor  # 새로운 FPS 계산

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # 새로운 비디오 파일 작성
    video_writer = cv2.VideoWriter(output_video, cv2.VideoWriter_fourcc(*'mp4v'), new_fps, (width, height))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        video_writer.write(frame)

    cap.release()
    video_writer.release()
    print(f"1.75x video saved to {output_video}")

def move_drone(drone):
   
    sleep(1)
    drone.takeoff()  
    drone.move_forward(90)
    drone.land()
  
drone = Tello()
drone.connect()

output_video = 'tello_flight_video1.mp4'  # 원본 동영상 파일 이름
speedup_output_video = 'tello_flight_video_1.75x2.mp4'  # 1.75배속 동영상 파일 이름

# 드론 이동 스레드 시작
move_thread = threading.Thread(target=move_drone, args=(drone,))
move_thread.start()
# 스트리밍 및 녹화 스레드 시작
stream_thread = threading.Thread(target=stream_video_and_record, args=(drone, output_video))
stream_thread.start()
    
# 스레드가 종료될 때까지 기다림
move_thread.join()
stream_thread.join()

# 드론 연결 종료
drone.end()

# 프로그램 종료 시 모든 OpenCV 창을 닫음
cv2.destroyAllWindows()

# 1.75배속으로 동영상 변환
speed_up_video(output_video, speedup_output_video, 1.75)

# 동영상 경로 및 열기(파일경로:저장하고 싶은 위치)
file_path = r'C:\Users\son\Desktop\Drone_github\tello_flight_video_1.75x2.mp4'
subprocess.run(['start', file_path], shell=True)



