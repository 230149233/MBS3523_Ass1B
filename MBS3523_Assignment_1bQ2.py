import cv2
cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    width = cam.get(3)
    height = cam.get(4)
    
    frameBlur = cv2.GaussianBlur(frameGray,(5,5),0)
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    frameCanny = cv2.Canny(frame, 100, 300)
    cv2.imshow("Webcam", frame)
    cv2.imshow("Webcam Gaussian Blur", frameBlur)
    cv2.imshow("Webcam HSV", frameHSV)
    cv2.imshow("Webcam Canny Edges", frameCanny)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
