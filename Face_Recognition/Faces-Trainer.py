import face_recognition
import cv2
import os
import pickle

path = 'images/face_recognition_samples'
images = []
testNames = []
myList = os.listdir(path)
file_names = "face_names.pkl"
fileobj_names = open(file_names, 'wb')
file_encodings = "face_encodings.pkl"
fileobj_encodings = open(file_encodings, 'wb')


def findEncodings(images):
    encode_list = []
    for img_encode in images:
        img_encode = cv2.cvtColor(img_encode, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img_encode)[0]
        encode_list.append(encode)
    return encode_list


for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    testNames.append(os.path.splitext(cl)[0])
print(testNames)
encodedListKnown = findEncodings(images)
pickle.dump(encodedListKnown, fileobj_encodings)
pickle.dump(testNames, fileobj_names)

fileobj_encodings.close()
fileobj_names.close()
