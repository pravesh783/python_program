import cv2
import numpy as np
face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cap=cv2.VideoCapture(1)
count = 0
def face_extractor(img):
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray,1.3,5)
    if faces ==():
        return None
    else:
        for(x,y,w,h) in faces:
            croped_face=img[y:y+h,x:x+w]
            return croped_face
while True:    
    ret,frame=cap.read()
    if ret:
        if face_extractor(frame) is not None:
            count+=1
            face=cv2.resize(face_extractor(frame),(200,200))
            face= cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
            file_name_path = 'C:/Users/pravesh/Desktop/Program2/face/user'+str(count)+'.jpg'
            cv2.imwrite(file_name_path,face)
            cv2.putText(face,str(count),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
            cv2.imshow("FACE Crpper",face)
        else:
            print("Face not found")
            pass
        if cv2.waitKey(1)==13 or count==100 or 0xFF==ord('q'):
            break
cap.release()
cv2.destroyAllWindows()
print("Collecting Sample Complete!!!!!")
