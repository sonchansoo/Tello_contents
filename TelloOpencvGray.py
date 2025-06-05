#OpenCV를 사용하여 흑백 영상으로 변환
import cv2
from djitellopy import Tello

# Tello 드론 초기화
tello = Tello()
tello.connect()
tello.streamon()

# 비디오 캡처 시작
cap = cv2.VideoCapture('udp://0.0.0.0:11111')

while True:
    ret, frame = cap.read()
    
    if ret:
        # OpenCV를 사용한 영상 처리 (예: 흑백 변환)
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # lab_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
        # luv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2LUV)
        # xyz_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2XYZ)
        # hls_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS)


        # 결과 출력
        cv2.imshow("Tello Video", gray_frame)
    
    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 종료
cap.release()
cv2.destroyAllWindows()
tello.streamoff()
