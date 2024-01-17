from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk 
import os
#from student import Student
from Train import Train
#from face_recognition import Face_Recognition

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1600x800+0+0")
        self.root.title("Face Recognition System")

        ### 1st image
        i1=Image.open(r'D:\projects source code\download (1).jpg')
        i1=i1.resize((500,130),Image.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(i1)
        f1=Label(self.root,image=self.photoimg11)
        f1.place(x=0, y=0,width=500,height=130)

        ## 2nd image
        i2=Image.open(r'D:\projects source code\download (1).jpg')
        i2=i2.resize((700,130),Image.LANCZOS)
        self.photoimg12=ImageTk.PhotoImage(i2)
        f1=Label(self.root,image=self.photoimg12)
        f1.place(x=500, y=0,width=600,height=130)

        ## 3rd image
        i3=Image.open(r'D:\projects source code\download (1).jpg')
        i3=i3.resize((500,130),Image.LANCZOS)
        self.photoimg13=ImageTk.PhotoImage(i3)
        f1=Label(self.root,image=self.photoimg13)
        f1.place(x=1030, y=0,width=500,height=130)

        ## bg image
        bg=Image.open(r'D:\projects source code\download.jpg')
        bg=bg.resize((1530,710),Image.LANCZOS)
        self.photoimg14=ImageTk.PhotoImage(bg)  
        f1=Label(self.root,image=self.photoimg14)
        f1.place(x=0, y=130, width=1530,height=710)

        ### label of Face recognition attendece system
        title_lbl=Label(background= "black",text="FACE  RECOGNITION  ATTENDANCE  SYSTEM  SOFTWARE",font=("times new roman",25,"bold"),fg="red")
        title_lbl.place(x=0,y=3, width=1600, height=45)

        #student button
        img1=Image.open(r'D:\projects source code\download (1).jpg')
        img1=img1.resize((220,220),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)  

        b1=Button(image=self.photoimg1,cursor="hand2")
        b1.place(x=200,y=160,width=220,height=220)
        b1_1=Button(text="Student",cursor="hand2",font=("times new roman",15,"bold"),bg="red",)
        b1_1.place(x=200,y=379,width=220,height=40)

        #face detector button
        img2=Image.open(r'D:\projects source code\download (1).jpg')
        img2=img2.resize((220,220),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)  

        b2=Button(image=self.photoimg2,cursor="hand2")
        b2.place(x=500,y=160,width=220,height=220)
        b2_1=Button(text="Face Detector",cursor="hand2",font=("times new roman",15,"bold"),bg="red",)
        b2_1.place(x=500,y=379,width=220,height=40)

        #Attendence button
        img3=Image.open(r'D:\projects source code\download (1).jpg')
        img3=img3.resize((220,220),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)  

        b3=Button(image=self.photoimg3,cursor="hand2")
        b3.place(x=800,y=160,width=220,height=220)
        b3_1=Button(text="Attendance",cursor="hand2",font=("times new roman",15,"bold"),bg="red",)
        b3_1.place(x=800,y=379,width=220,height=40)

        #Help desk button
        img4=Image.open(r'D:\projects source code\download (1).jpg')
        img4=img4.resize((220,220),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)  

        b4=Button(image=self.photoimg4,cursor="hand2")
        b4.place(x=1100,y=160,width=220,height=220)
        b4_1=Button(text="Help Desk",cursor="hand2",font=("times new roman",15,"bold"),bg="red",)
        b4_1.place(x=1100,y=379,width=220,height=40)

        
        #############BOTTOM BUTTON########
        #Train face button
        img5=Image.open(r'D:\projects source code\download (1).jpg')
        img5=img5.resize((230,255),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)  

        b5=Button(image=self.photoimg5,cursor="hand2")
        b5.place(x=200,y=480,width=220,height=220)
        b5_1=Button(text="Train Data",cursor="hand2",font=("times new roman",15,"bold"),bg="red",)
        b5_1.place(x=200,y=699,width=220,height=40)

        #photos
        img6=Image.open(r'D:\projects source code\download (1).jpg')
        img6=img6.resize((220,235),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)  

        b6=Button(image=self.photoimg6,cursor="hand2")
        b6.place(x=500,y=480,width=220,height=220)
        b6_1=Button(text="Photos",cursor="hand2",font=("times new roman",15,"bold"),bg="red",)
        b6_1.place(x=500,y=699,width=220,height=40)

        #Developers 
        img7=Image.open(r'D:\projects source code\download (1).jpg')
        img7=img7.resize((220,220),Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)  

        b7=Button(image=self.photoimg7,cursor="hand2")
        b7.place(x=800,y=480,width=220,height=220)
        b7_1=Button(text="Developers",cursor="hand2",font=("times new roman",15,"bold"),bg="red",)
        b7_1.place(x=800,y=699,width=220,height=40)

        #Exit button
        img8=Image.open(r'D:\projects source code\download (1).jpg')
        img8=img8.resize((220,245),Image.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)  

        b8=Button(image=self.photoimg8,cursor="hand2")
        b8.place(x=1100,y=480,width=220,height=220)
        b8_1=Button(text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="red",)
        b8_1.place(x=1100,y=699,width=220,height=40)




   

    def open_img(self):
        os.startfile("data")






 ################ Funcion buttons


    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    '''def Student(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)'''
    
    '''def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)'''




if __name__== "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
