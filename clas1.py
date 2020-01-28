import cv2
import sys
import dlib
import time
import datetime
import glob
from threading import Thread
class MyThread1(Thread):
    def __init__(self, arg1, arg2, arg3):
        Thread.__init__(self)
        self.detector = arg1
        self.sp = arg2
        self.facerec = arg3

        self.dict = {}

        
    def run(self):
        detector = self.detector
        sp = self.sp
        facerec = self.facerec

        face_descriptor_it = []
        face_descriptor_name = []
    
        now1 = datetime.datetime.now()
        my_file = open("log/log.txt", "a")
        my_file.write("Начало работы: "+now1.strftime("%d-%m-%Y %H:%M")+"\n")
        print("Начало работы: "+now1.strftime("%d-%m-%Y %H:%M"))

        for fil in glob.iglob('foto/**/*.jpg', recursive=True):
            img = dlib.load_rgb_image(fil)
     
            my_file.write("В обработке файлы цели: "+fil+"\n")
            print("В обработке файлы цели: "+fil)
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

        print("Можно работать!")
        my_file.close()
    
