import cv2
import numpy as np
from djitellopy import Tello

# Tello 드론 연결
tello = Tello()
tello.connect()
tello.streamon()

# ArUco 마커 사전 설정 (5x5_1000 사전 사용)
aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_100)
parameters = cv2.aruco.DetectorParameters_create()

# 카메라 피드 받기
frame_read = tello.get_frame_read()

# 원하는 프레임 크기 설정
width, height = 960, 720

while True:
    # 프레임 읽기
    frame = frame_read.frame
    
    if frame is not None:
        # 프레임 크기 조정
        frame = cv2.resize(frame, (width, height))
        
        # 그레이스케일 변환
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 화면에 프레임 출력 (ArUco 탐지 전)
        cv2.imshow('Tello Stream', frame)
        
        # ArUco 마커 탐지 (5x5 사전 사용)
        corners, ids, rejected = cv2.aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
        
        # 마커가 감지되었을 때 처리
        if ids is not None:
            # 마커 그리기
            cv2.aruco.drawDetectedMarkers(frame, corners, ids)
            
            # 감지된 모든 마커의 ID 출력
            for i in range(len(ids)):
                print(f"Detected ArUco marker ID: {ids[i][0]}")
                
                # 마커 ID를 프레임에 출력
                cv2.putText(frame, f"ID: {ids[i][0]}", 
                            (int(corners[i][0][0][0]), int(corners[i][0][0][1]) - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            # ArUco 마커가 감지된 프레임을 다시 출력
            cv2.imshow('Tello ArUco Detection', frame)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 리소스 정리
tello.streamoff()
cv2.destroyAllWindows()