import shutil
import cv2
import os


def start(name="image", quality=5):
    filepath = "image_or_video_scanner/data"
    try:
        shutil.rmtree(filepath)
    except Exception as error:
        pass
    os.mkdir(filepath)

    matrix_rbg = cv2.imread(os.path.join("image_or_video_scanner/static", "example.jpg"))
    height, width, _ = matrix_rbg.shape
    gray = cv2.cvtColor(matrix_rbg, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier("image_or_video_scanner/static/cascadeHaare.xml")
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    face1 = {"x": 0, "y": 0, "h": 0, "w": 0}
    for i in faces:
        face1["x"] = i[0]
        face1["y"] = i[1]
        face1["h"] = i[2]
        face1["w"] = i[3]
    multiply = int(50 * (height / 1000))
    cropped = gray[
              0 + face1["y"] - int(multiply * 1.5):0 + face1["y"] + face1["h"] + int(multiply * 0.8),
              0 + face1["x"] - multiply:0 + face1["x"] + face1["w"] + multiply
              ]
    cv2.imwrite(os.path.join(filepath, "new_" + f'{name}.jpg'), cropped, [int(cv2.IMWRITE_JPEG_QUALITY), quality])


if __name__ == '__main__':
    pass
