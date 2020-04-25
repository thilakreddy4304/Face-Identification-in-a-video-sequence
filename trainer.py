import os
import cv2
import numpy as np
from PIL import Image

recognizer=cv2.face.LBPHFaceRecognizer_create()
path="samples"

def getImagewithID(path):
	imagepaths=[os.path.join(path,f) for f in os.listdir(path)]
	face=[]
	ids=[]
	for imagepath in imagepaths:
		faceimg=Image.open(imagepath).convert("L")
		facenp=np.array(faceimg,"uint8")
		ID=int(os.path.split(imagepath)[-1].split(".")[1])
		face.append(facenp)
		print(ID)
		ids.append(ID)
		cv2.imshow("training", facenp)
		cv2.waitKey(1)
	return ids, face

ids,face=getImagewithID(path)
recognizer.train(face,np.array(ids))
recognizer.save("yml/trainingdata.yml")
