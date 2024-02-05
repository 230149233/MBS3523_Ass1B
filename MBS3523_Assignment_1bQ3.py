import cv2
cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    width = cam.get(3)
    height = cam.get(4)

    frame_2 = cv2.flip(frame,1)

    top_row = cv2.hconcat([frame,frame_2])
    bottom_row = cv2.flip(top_row,0)
    combine_frame = cv2.vconcat([top_row,bottom_row])

    cv2.imshow('Frame',combine_frame)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
