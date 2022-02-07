import numpy as np
import cv2

'''
# 그레이스케일 이미지 생성 (쓰레기 값 넣어서)
img_grey_garbage = np.empty((240, 320), dtype=np.uint8)
# 칼라 이미지 생성 (쓰레기 값)
img_col_garbage = np.empty((240, 320, 3), dtype=np.uint8)
# 0, 1로 값 채우기
img_zero = np.zeros((240, 320, 3), dtype=np.uint8)
img_one = np.ones((240, 320, 3), dtype=np.uint8)
# 특정 값으로 채우기
img_full = np.full((240, 320), 128, dtype=np.uint8)

cv2.imshow('grey', img_grey_garbage)
cv2.imshow('color', img_col_garbage)
cv2.imshow('zero', img_zero)
cv2.imshow('one', img_one)
cv2.imshow('full', img_full)
'''

# 새 영상 생성하기
img1 = cv2.imread('HappyFish.jpg')

img_copy = img1.copy()
img2 = img1

## 부분 copy
img_copy_part = img1[40:120, 30:150].copy()

# img.copy()는 데이터를 공유 하는 것이 아닌 현재 상황을 그대로 복사본을 생성
# 그냥 img2 = img 를 할 경우 -> 참조개념
cv2.imshow('img1', img1)
cv2.imshow('img2', img_copy)
cv2.imshow('img3', img2)
cv2.imshow('img4', img_copy_part)

cv2.waitKey()