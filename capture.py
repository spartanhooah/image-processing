import cv2, time

video = cv2.VideoCapture(0)

a = 1
while True:
    a = a + 1
    check, frame = video.read()

    # time.sleep(3)

    cv2.imshow("Capturing", frame)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

video.release()

cv2.destroyAllWindows()

print(a)