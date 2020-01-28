import cv2
import subprocess
import dlib
import clas1
import clas
cam = cv2.VideoCapture(0)
#cam.open('rtsp://admin:admin12345678@192.168.83.1:554/cam/realmonitor?channel=6&subtype=1')



predictor_path = "shape_predictor_68_face_landmarks.dat"
#predictor_path = "shape_predictor_5_face_landmarks.dat"

face_rec_model_path = 'dlib_face_recognition_resnet_model_v1.dat'

detector = dlib.get_frontal_face_detector()

sp = dlib.shape_predictor(predictor_path)
facerec = dlib.face_recognition_model_v1(face_rec_model_path)

color_green = (0,255,0)
line_width = 3

f=clas1.MyThread1(detector, sp, facerec)
f.start()
f.join()

#subprocess.call("python cam.py frame", shell=True)
while(cam.isOpened()):
    ret_val, img = cam.read()
    rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    dets = detector(rgb_image, 1)
    for k, d in enumerate(dets):
        cv2.rectangle(img,(d.left(), d.top()), (d.right(), d.bottom()), color_green, line_width)
   
        shape = sp(rgb_image, d)
        face_descriptor_fram = facerec.compute_face_descriptor(rgb_image, shape)
        c = clas.MyThread(face_descriptor_fram, f.dict, rgb_image, img)
        c.start()
      
    cv2.imshow('my webcam', img)    
    if cv2.waitKey(1) & 0xFF == ord('q'):
         break
#cam.release()
cv2.destroyAllWindows()
