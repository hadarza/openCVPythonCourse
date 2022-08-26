from turtle import heading
import cv2 as cv

img = cv.imread('Resources/Photos/cat_large.jpg')
cv.imshow('Cat',img)

def rescaleFrame(frame,scale = 0.75):
    # video,pictures and live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

def changeRes(width,height):
    #live video 
    capture.set(3,width)
    capture.set(4,height)


frameResizabled = rescaleFrame(img,0.4)
cv.imshow(' resize img',frameResizabled)


capture = cv.VideoCapture('Resources/Videos/dog.mp4')
while True:
    isTrue,frame = capture.read()
    frameResizabled = rescaleFrame(frame,0.4)
    cv.imshow('Video',frame)
    cv.imshow(' resize Video',frameResizabled)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
    
capture.release()
cv.destroyAllWindows()