########## face_recognition.py#######

from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk 
from tkinter import messagebox
import mysql.connector
import cv2
import os 
import numpy as np


class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1300x700+0+0")
        self.root.title("Face Recognition System")


        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",25,"bold"),fg="yellow",bg="blue")
        title_lbl.place(x=0,y=0, width=1500, height=45)

        save_btn=Button(self.root,text="Click  Here",width=16,cursor="hand2",font=("times new roman",25,"bold"),bg="red",fg="white")
        save_btn.place(x=0,y=350, width=1500, height=45)


        # ===== face recgnition =========

    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeigbhours,color,text,clf):
            gray_image=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeigbhours)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])


if __name__: "__main__"
root=Tk()
obj=Face_Recognition(root)
root.mainloop()