#Identify pupils. Based on beta 1

import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0) 	#640,480
w = 640
h = 480

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
	
		#downsample
		#frameD = cv2.pyrDown(cv2.pyrDown(frame))
		#frameDBW = cv2.cvtColor(frameD,cv2.COLOR_RGB2GRAY)
	
		#detect face
		frame = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
		faces = cv2.CascadeClassifier('haarcascade_eye.xml')
		detected = faces.detectMultiScale(frame, 1.3, 5)
	
		#faces = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
		#detected2 = faces.detectMultiScale(frameDBW, 1.3, 5)
		
		eye_frame = frame
		pupilO = frame
		windowClose = np.ones((5,5),np.uint8)
		windowOpen = np.ones((2,2),np.uint8)
		windowErode = np.ones((2,2),np.uint8)

		#draw square
		eye_list = []
		for (x,y,w,h) in detected:
			pupil_frame = frame[(y+h/3):(y+h-h/3), x+w/3:(x+w-w/3)]
			a,b,c,d = cv2.minMaxLoc(~pupil_frame)
			processed = cv2.medianBlur(pupil_frame,5)
			processed = cv2.equalizeHist(processed)
			#cv2.circle(processed, (d), 5, (0,0,255), 5)
			#cv2.imshow('frame2',processed)
			processed = cv2.Canny(processed, 100, 300, 10, L2gradient=True)
			#cv2.imshow('frame1',processed)
			circles = cv2.HoughCircles(processed,cv2.cv.CV_HOUGH_GRADIENT,2,20,param1=300,param2=10,minRadius=2,maxRadius=(w/4))
			circles = np.asarray(circles)

			eye_frame = frame[(y+h/3):(y+h-h/3), x-2:(x+w+2)]
			gray = np.float32(eye_frame)
			corners = cv2.goodFeaturesToTrack(gray,25,0.02,0)
			corners = np.int0(corners)
			xmin, xmax = 1000,0
			for i in corners:
				xr,yr = i.ravel()
				xmin = min(xr, xmin)
				xmax = max(xr, xmax)
				cv2.circle(eye_frame, (xr, yr), 2, (255,255,255), 1)
			xmiddle = x -2 + (xmax + xmin)/2
			cv2.imshow('frame1',eye_frame)

			if circles.size > 1 :
				for i in circles:
					cv2.circle(pupil_frame, (i[0][0],i[0][1]), i[0][2], (255,255,255), 2)
					cv2.circle(pupil_frame, (i[0][0],i[0][1]), 2, (255,255,255), 3)
					eye_center  = x+w/3 + i[0][0] - xmiddle
					eye_list.append(eye_center)

		eye_angle = 0
		if len(eye_list) > 0:
			eye_angle = sum(eye_list)/len(eye_list)
			print eye_angle
		#show picture

		cv2.imshow('frame',pupilO)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	
	#else:
		#break

# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()


