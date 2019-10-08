import cv2
import facedetect

template = './haar/haarcascade_frontalface_default.xml'

det = facedetect.FaceDetector(template)

cap = cv2.VideoCapture(0)

while 69:
    _, frame = cap.read()
    img = det.detect_draw(frame)
    cv2.imshow("Bruh",img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()