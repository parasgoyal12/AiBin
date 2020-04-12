import tensorflow as tf
#import serial
model=tf.keras.models.load_model('complete_model.h5')

import cv2

from tensorflow.keras.preprocessing import image
import numpy as np


cap=cv2.VideoCapture(2)
#	ser=serial.Serial('COM6',9600)
while(True):
	ret,frame=cap.read()
	cv2.imshow('frame',frame)
	frame=cv2.resize(frame,(224,224))
	frame = np.expand_dims(np.array(frame)/255, axis=0)

	classes=model.predict(frame)



	print(classes[0])
	val=np.argmax(classes[0])
	# if classes[0]>1-thresh:
	# 	print("NonBiodegradable")
	# 	ser.write(b'N')
	# elif classes[0]<thresh:
	# 	print("Biodegradable")
	# 	ser.write(b'B')
	# else:
	# 	print("None")
	# 	ser.write(b 'C')
	if val== 0:
		print("Biodegradable")
		#ser.write(b'B')
	if val==1:
		print("NonBiodegradable")
		#ser.write(b'N')
	if val==2:
		print("None")
		#ser.write(b'C')

	if cv2.waitKey(200) & 0xFF ==ord('q'):
		break


#ser.write('C')
cap.release()
cv2.destroyAllWindows()

	
