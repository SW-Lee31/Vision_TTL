import numpy as np
import cv2

img = np.full((400, 400, 3), 255, np.uint8)

# cv2.line(srcimg, 시작좌표, 끝좌표, 색상{B, G, R}, 선 굵기, 선 형태)
cv2.line(img, (50, 50), (200, 50), (0, 0, 255), 5)
cv2.line(img, (50, 60), (150, 160), (0, 0, 128))

# cv2.rectangel(srcimg, 꼭지점4개정보{튜플}, 색상, 선굵기, 선형태)
# cv2.rectangle(srcimg, 꼭지점좌상, 꼭지점우하, 색상, 선굵기, 선형태)
# 선굵기에 -1을 주면 내부를 채움
cv2.rectangle(img, (50, 200, 150, 100), (0, 255, 0), 2)
cv2.rectangle(img, (70, 220), (180, 280), (0, 128, 0), -1)

# cv2.circle(srcimg, 원중심, 반지름, 선굵기, 선형태)
# 선형태를 cv2.LINE_8이 default임, cv2.LINE_AA를 주면 부드럽게 활용 가능
cv2.circle(img, (300, 100), 30, (255, 255, 0), -1, cv2.LINE_AA)
cv2.circle(img, (300, 100), 60, (255, 0, 0), 3, cv2.LINE_AA)

# cv2.polylines(srcimg, [pts]{다각형 좌표 리스트}, 폐곡선(True -> 시작, 끝점 이어줌, False -> 열어 줌), 색상, 선굵기, 선형태)
pts = np.array([[250, 200], [300, 200], [350, 300], [250, 300]])
cv2.polylines(img, [pts], False, (255, 0, 255), 2)

# cv2.putText(imgsrc, 입력문자열, 시작좌표, 폰트종류, 폰트크기, 색상, 선굵기, 선형태)
text = 'Hello? OpenCV ' + cv2.__version__
cv2.putText(img, text, (50, 350), cv2.FONT_HERSHEY_SIMPLEX, 0.8, 
            (0, 0, 255), 1, cv2.LINE_AA)


cv2.imshow("img", img)
cv2.waitKey()
cv2.destroyAllWindows()

