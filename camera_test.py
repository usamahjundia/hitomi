import camera
import cv2

cmr = camera.Camera(0)

while True:
    frame = cmr.read()
    cv2.imshow("bruh",frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
        
cv2.destroyAllWindows()