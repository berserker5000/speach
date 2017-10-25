import cv2

faceCascade = cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_eye.xml')

img = cv2.VideoCapture(0)

while (1):
    _, f = img.read()
    gray = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.3, 5)

    pressedKey = cv2.waitKey(2)
    if pressedKey == ord('Q'):
        cv2.destroyAllWindows()
        exit(0)

    for (x, y, w, h) in faces:
        cv2.rectangle(f, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = f[y:y + h, x:x + w]

    cv2.imshow('Test', f)
    if cv2.waitKey(25) == 27:
        break

cv2.destroyAllWindows()
img.release()