from djitellopy import Tello

tello = Tello()

# 드론에 연결
tello.connect()  

# 드론의 영상 스트리밍을 켬
tello.streamon()

# 프레임 리더 객체를 가져옴
frame_reader = tello.get_frame_read()
# 드론으로부터 프레임을 가져옴
frame = frame_reader.frame

# 드론의 영상 스트리밍 중지  
tello.streamoff()
   

# 드론 연결 종료
tello.end()


