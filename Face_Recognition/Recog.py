import cv2
import numpy as np
import face_recognition
import os
import pickle

path = 'images/face_recognition_samples'
images = []
myList = os.listdir(path)
fileEncodings = "face_encodings.pkl"
fileobj_encodings = open(fileEncodings, 'rb')
fileNames = "face_names.pkl"
fileobj_names = open(fileNames, 'rb')
encodedListKnown = pickle.load(fileobj_encodings)
testNames = pickle.load(fileobj_names)
fileobj_names.close()
fileobj_encodings.close()

cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    imgSmall = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgSmall = cv2.cvtColor(imgSmall, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgSmall)
    encodingCurFrame = face_recognition.face_encodings(imgSmall, facesCurFrame)
    faceDis = []
    for encodeFace, faceLoc in zip(encodingCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodedListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodedListKnown, encodeFace)
        matchIndex = np.argmin(faceDis)
        if matches[matchIndex]:
            name = testNames[matchIndex].upper()
            # print(name)
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            if 9 < len(name) < 16:
                cv2.rectangle(img, (x1 - 25, y1-30), (x2 + 25, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1 - 25, y2 - 35), (x2 + 25, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name, (x1 - 19, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 255, 255), 2)
            elif len(name) > 16:
                cv2.rectangle(img, (x1 - 30, y1-30), (x2 + 30, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1 - 30, y2 - 35), (x2 + 30, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name, (x1 - 24, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 255, 255), 2)
            else:
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
        else:
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, "UNKNOWN", (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)

    cv2.imshow('webcam', img)
    cv2.waitKey(1)
