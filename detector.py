import cv2
faceDetect = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
cap = cv2.VideoCapture(0)
recognizer=cv2.face.LBPHFaceRecognizer_create()
recognizer.read("yml/trainingdata.yml")
id=0
font=cv2.FONT_HERSHEY_DUPLEX
while True:
    check, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), [255, 0, 0], 2)
        cv2.putText(frame,(str(id)),(x,y),font,1,[255,255,0],2)
        id,conf=recognizer.predict(gray[y:y+h,x:x+w])
        #cv2.putText(frame,int(conf),(x,y),font,1,[255,255,0],2)
        if conf<=80:       
            if(id==1):
                id="thilak"
                print(conf)
            elif(id==2):
                id="modi"
                print(conf)       
        else:
            id="unknown"
            print(conf)
    cv2.imshow("feed", frame)
    if(cv2.waitKey(1)==ord('q')):
        break
cap.release()

