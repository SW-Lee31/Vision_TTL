import sys
import cv2

'''
# 카메라 열기
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera open failed!")
    sys.exit()

# 카메라 프레임 크기 출력
print('Frame width:', int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
print('Frame height:', int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

# 카메라 프레임 처리
while True:
    ret, frame = cap.read()

    if not ret:
        break

    inversed = ~frame  # 반전

    cv2.imshow('frame', frame)
    cv2.imshow('inversed', inversed)

    if cv2.waitKey(10) == 27:
        break

cap.release()
cv2.destroyAllWindows()
'''

cap = cv2.VideoCapture()
cap.open(0)
# == cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture('video1.mp4')

if not cap.isOpened():
    print('camera open failed!')
    sys.exit()

# cap.get() -> 속성 받아오기
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(w, h)

# cap.set() -> 속성 입력
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

while True:
    retval, frame = cap.read() # 한프레임씩 받아옴 -> return value (retval, image)
    
    if not retval:
        break

    # 영상에서 윤곽선 추출
    edge = cv2.Canny(frame, 50, 150)

    cv2.imshow('frame', frame)
    cv2.imshow('edge', edge)

    if cv2.waitKey(20) == 27:
        break

cap.release()
cv2.destroyAllWindows()