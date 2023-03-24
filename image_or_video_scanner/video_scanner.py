import cv2


def start():
    cap = cv2.VideoCapture('image_or_video_scanner/static/example.mp4')
    while cap.isOpened():
        ret, matrix_rbg = cap.read()
        if ret:
            height, width, _ = matrix_rbg.shape
            face_cascade = cv2.CascadeClassifier("image_or_video_scanner/static/cascadeHaare.xml")

            gray = cv2.cvtColor(matrix_rbg, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(
                gray,
                scaleFactor=1.3,
                minNeighbors=5,
                minSize=(20, 20),
                flags=cv2.CASCADE_SCALE_IMAGE
            )
            for (x, y, w, h) in faces:
                cv2.rectangle(matrix_rbg, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.imshow('обнаружение', matrix_rbg)

            if cv2.waitKey(5) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    pass
