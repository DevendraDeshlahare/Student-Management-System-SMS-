########### train.py ############

from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk 
from tkinter import messagebox
import mysql.connector
import cv2
import os 
import numpy as np


class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1300x700+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="TRAIN  DATA  SET",font=("times new roman",25,"bold"),fg="yellow",bg="blue")
        title_lbl.place(x=0,y=0, width=1500, height=45)



        save_btn=Button(self.root,text="Train Data",command=self.train_classifier,width=16,cursor="hand2",font=("times new roman",25,"bold"),bg="red",fg="white")
        save_btn.place(x=0,y=350, width=1500, height=45)

       # b1_3=Button(text="Train Data",cursor="hand2",command=self.train_data,fg="red",font=("times new roman",15,"bold"),bg="darkblue",)
        #b1_3.place(x=200,y=400,width=220,height=220)




    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir) for file in os.listdir(data_dir)]


        faces=[]
        Rolls=[]

        for image in path:
            img=Image.open(image).convert('L')   #gray scale image
            imageNP=np.array(img,'unit8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNP)
            Rolls.append(Rolls)
            cv2.imshow("Trainnig",imageNP)
            cv2.waitKey(1)==13
        Rolls=np.array(Rolls)

        ##### Train the class and save ###############

        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,Rolls)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!")







if __name__: "__main__"
root=Tk()
obj=Train(root)
root.mainloop()