from tkinter.messagebox import NO
import cv2
import sys

print('hello, openCV', cv2.__version__)

# imread -> 이미지 리드 param1 -> filename, param2 -> flag: 옵션(default: imread_color)
img = cv2.imread('cat.bmp')
# = img = cv2.imread('cat.bmp', cv2.IMREAD_COLOR) cv2.IMREAD_GRAYSCLAE(그레이스케일), cv2.IMREAD_UNCHANGED(투명한 png)
imggray = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)
# imwrite -> 영상 쓰기
cv2.imwrite('cat_gray.png', imggray)

if img is None:
    print('image load failed')
    sys.exit()

# namedWindow -> 창을 하나 띄워주는 함수 param2 -> flag(default : cv2.WINDOW_AUTOSIZE) cv2.WINDOW_NORMAL (사이즈 조절 가능)
cv2.namedWindow('showimg')
# imshow -> 이미지 창에 로드 !! waitkey가 동반되어야 화면 출력 가능!!
cv2.imshow('showimg', img)
cv2.waitKey()

''' 특정 키로 waitkey 지정
while True:
    if cv2.waitkey() == ord('q'):
        break
'''

cv2.destroyAllWindows()
# = cv2.destroyWindow('showimg') -> 특정 창 종료