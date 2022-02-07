import sys
from tkinter.messagebox import NO
import cv2

img1 = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('cat.bmp', cv2.IMREAD_COLOR)

if img1 is None or img2 is None:
    print('Image load error')
    sys.exit()

print(type(img1))
print(img1.shape)
print(img2.shape)
print(img1.dtype)
print(img2.dtype)

# img1.ndim or len(img1.shape) == 2 -> grayscale
# img2.ndim or len(img1.shape) == 3 -> color

## width, height 구하기
h1, w1 = img1.shape[:2]
# color는 3개이므로 앞의 2개만 출력
h2, w2 = img2.shape[:2]

print('img1 : {} x {}, img2 : {} x {}'.format(w1, h1, w2, h2))

'''
# 색상 임의 변경 (속도가 엄청 느리므로 지양 opencv, numpy 제공하는 유틸이 있음)
for y in range(h1):
    for x in range(w1):
        img1[y, x] = 0
        img2[y, x] = (0, 255, 255)


== 동일
img1[:, :] = 0
img2[:, :] = (0, 0, 255)
'''
