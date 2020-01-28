import cv2
import sys
import dlib
import time
import datetime
import glob
from threading import Thread
class MyThread1(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.arg1 = "shape_predictor_68_face_landmarks.dat"
        #self.arg1 = "shape_predictor_5_face_landmarks.dat"
        self.arg2 = 'dlib_face_recognition_resnet_model_v1.dat'
        self.dict = {}
        
    def run(self):
        predictor_path = self.arg1
        face_rec_model_path = self.arg2
        detector = dlib.get_frontal_face_detector()
        sp = dlib.shape_predictor(predictor_path)
        facerec = dlib.face_recognition_model_v1(face_rec_model_path)
        face_descriptor_it = []
        face_descriptor_name = []
    
        now1 = datetime.datetime.now()
        my_file = open("log/log.txt", "a")
        my_file.write("Начало работы: "+now1.strftime("%d-%m-%Y %H:%M")+"\n")

        for fil in glob.iglob('foto/**/*.jpg', recursive=True):
            img = dlib.load_rgb_image(fil)
     
            my_file.write("В обработке файлы цели: "+fil+"\n")
            try:
                dets = detector(img)
                for k, d in enumerate(dets):
                    shape = sp(img, d)
                    face_descriptor_it.append(facerec.compute_face_descriptor(img, shape))
                    face_descriptor_name.append(fil)
                    self.dict = {'name': face_descriptor_name, 'val': face_descriptor_it}
                    #print(face_descriptor_name, "++++++", face_descriptor_it, "\n\n\n\n\n\n\n")
                    #self.dict.update(dict2)
            except:
                pass
           
        my_file.close()
    
