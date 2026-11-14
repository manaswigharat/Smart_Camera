
import cv2

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Camera not detected!")
else:
    print("Camera started successfully!")

    while True:
        success, frame = camera.read()

        if not success:
            print("Unable to read camera")
            break

        cv2.imshow("My First Camera Test", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

camera.release()
cv2.destroyAllWindows()
