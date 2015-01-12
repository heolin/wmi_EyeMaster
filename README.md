# wmi_EyeM@ster

eye_server.py - main program, wraps main pipeline
face_detect.py - module responsible for detecting faces and eyes, as a result it return regions of image.
frame_processor.py - module responsible for processing regions with faces and eyes to determine direction of eyes.
input_handle.py - module responsible for mapping input into API from
message_server.py - module responsible for handling API messages 

haarcascade_frontalface_default.xml - haar model trained to detect faces
haarcascade_eye.xml - haar model trained to detect eyes

README.md - this file
