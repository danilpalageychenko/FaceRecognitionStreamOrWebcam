import cv2
import telegram_send
import sys
from datetime import datetime
from threading import Thread
from time import sleep
from scipy.spatial import distance
class MyThread(Thread):
    def __init__(self, arg1, arg2, arg3, arg4):
        Thread.__init__(self)
        self.arg1 = arg1 
        self.arg2 = arg2
        self.arg3 = arg3
        self.arg4 = arg4
        self.ch = 0

    def run(self):
        i=0
        for det in self.arg2['val']:
            title = self.arg2['name'][i]
            t=title.split('\\')
            t1 = t[1].split('.')

            i=i+1
            a = distance.euclidean(det, self.arg1)
            if a < 0.55:
                cv2.imwrite('find/' + t1[0] + '.jpg', self.arg4)
                while self.ch < 2:
                    #sleep(0.5)
                    now = datetime.now()
                    last_line = open("log/log.txt").readlines()[-1]
                    str1 = last_line.rstrip().split(" ")

                    try:
                        last_data = datetime.strptime(str1[1] + " " + str1[2],'%d-%m-%Y %H:%M')
                    except Exception:
                        last_data = now

                    if t1[0] == str1[-1] and (now - last_data).seconds < 60:
                        exit()
                    else:
                        #print(t1[0] == str1[-1], "  ", (now - last_data).seconds < 60)
                        #print(t1[0], str1[-1], (now - last_data).seconds)
                        #print("qwe ", (now - last_data).seconds, t1[0] + " " + str1[-1] + "\n")
                     #with open("log/log.txt", "a") as my_file:
                        my_file = open("log/log.txt", "a")
                        my_file.write("ОБАНАРУЖЕННО:....Дата: " + now.strftime("%d-%m-%Y %H:%M") + " Призвище особи - " + t1[0] + "\n")
                        print("ОБАНАРУЖЕННО:....Дата: " + now.strftime("%d-%m-%Y %H:%M") + " Призвище особи - " + t1[0])
                        my_file.close()
                        with open('find/' + t1[0] + ".jpg", "rb") as f:
                            telegram_send.send(messages=["Дата: "+now.strftime("%d-%m-%Y %H:%M")+" Призвище особи - "+t1[0]], images=[f])
                        self.ch=self.ch+1
                        #print(t1[0] + " " + str1[-1], (now - last_data).seconds > 60)
                        #print()
                        #print((now - last_data).seconds)
                        #print(t1[0])
                        #print(str1[-1])
                        #data = datetime.strptime(str1[1] + " " + str1[2],'%d-%m-%Y %H:%M')
                        #print("qweqwe" + str1[1] + " " + str1[2] + "qweqweqwe")
                        #print((now - datetime.strptime(str1[1] + " " + str1[2],'%d-%m-%Y %H:%M')).seconds > 60)
                        #print((now - datetime.strptime(str1[1] + " " + str1[2],'%d-%m-%Y %H:%M')).seconds)

        
