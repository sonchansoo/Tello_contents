import cv2

# 이미지 로드
image_path = 'KakaoTalk_20241019_164400872.jpg'
image = cv2.imread(image_path)

# 이미지를 그레이스케일로 변환
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 그레이스케일 이미지 저장
output_path = 'KakaoTalk_20241019_164400872_gray.jpg'
cv2.imwrite(output_path, gray_image)