import sys
import cv2


# 마스크 영상을 이용한 영상 합성
src = cv2.imread('airplane.bmp', cv2.IMREAD_COLOR)
mask = cv2.imread('mask_plane.bmp', cv2.IMREAD_GRAYSCALE)
dst = cv2.imread('field.bmp', cv2.IMREAD_COLOR)


# opencv_logo 활용 4채널(마지막 채널(투명을) 마스크로 활용 가능)
''' 
src = cv2.imread('opencv-logo-white.png', cv2.IMREAD_UNCHANGED)
mask = src[:, :, -1] # 마지막 채널을 마스크로 활용
src = src[:, :, 0:3] # 남은 것을 소스로 활용 ~3 채널
dst = cv2.imread('field.bmp, cv2.IMREAD_COLOR)

# dst와 src의 크기가 다르기 때문에 변경 필요
h, w = src.shape[:2]
crop = dst[0:h, 0:w]

# .copy를 쓰면 해당 크기만큼 복사해서 새 파일로 활용

cv2.copyTo(src, mask, crop)
'''


if src is None or mask is None or dst is None:
    print('Image load failed!')
    sys.exit()

cv2.copyTo(src, mask, dst)
# dst[mask > 0] = src[mask > 0]

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('mask', mask)
cv2.waitKey()
cv2.destroyAllWindows()

# 알파 채널을 마스크 영상으로 이용
src = cv2.imread('cat.bmp', cv2.IMREAD_COLOR)
logo = cv2.imread('opencv-logo-white.png', cv2.IMREAD_UNCHANGED)

if src is None or logo is None:
    print('Image load failed!')
    sys.exit()

mask = logo[:, :, 3]    # mask는 알파 채널로 만든 마스크 영상
logo = logo[:, :, :-1]  # logo는 b, g, r 3채널로 구성된 컬러 영상
h, w = mask.shape[:2]
crop = src[10:10+h, 10:10+w]  # logo, mask와 같은 크기의 부분 영상 추출

cv2.copyTo(logo, mask, crop)
#crop[mask > 0] = logo[mask > 0]

cv2.imshow('src', src)
cv2.imshow('logo', logo)
cv2.imshow('mask', mask)
cv2.waitKey()
cv2.destroyAllWindows()
