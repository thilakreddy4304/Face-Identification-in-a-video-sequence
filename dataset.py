import cv2
faceDetect = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
cap = cv2.VideoCapture(0)
id = input("enter the id")
num = 0
while True:
    check, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        num+=1
        cv2.imwrite("samples/person."+str(id)+"."+str(num)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(frame, (x, y), (x + w, y + h), [255, 0, 0], 2)
    cv2.imshow("identifier", frame)
    if(num>59) or (cv2.waitKey(1)==ord('q')):
        break
cap.release()
