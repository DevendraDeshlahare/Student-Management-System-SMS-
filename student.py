
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk 
from tkinter import messagebox
import mysql.connector
import cv2
class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1300x700+0+0")
        self.root.title("Student Management System")
        ######VARIABles####
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_roll_num=StringVar()
        self.var_phone_num=StringVar()
        self.var_name=StringVar()
        self.var_gen=StringVar()
        title_lbl=Label(text="STUDENT  MANAGEMENT  SYSTEM",font=("times new roman",25,"bold"),fg="green",bg="black")
        title_lbl.place(x=0,y=0, width=1500, height=45)
        main_frame=Frame(bg="Gray",bd=2)
        main_frame.place(x=0,y=60,width=1500,height=700)
        ###LEFT LABEL
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Detail",font=("times new roman",20,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)
        ##current course
        current_course_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Current Course Informatiion",font=("times new roman",15,"bold"))
        current_course_frame.place(x=5,y=20 ,width=720,height=140)
        #Department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",13,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",10,"bold"),width=17,state="read only")
        dep_combo["values"]=("Select Department","CSE","EEE","IT","CIVIL","MECHANICAL")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        #course 
        course_label=Label(current_course_frame,text="Course",font=("times new roman",13,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",10,"bold"),width=17,state="read only")
        course_combo["values"]=("Select Course","B.tech","BE","MBA","SE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        #Semester
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",13,"bold"),bg="white")
        semester_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",10,"bold"),width=17,state="read only")
        semester_combo["values"]=("Select Semester","Sem-1","Sem-2","Sem-3","Sem-4","Sem-5","Sem-6","Sem-7","Sem-8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        #year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",13,"bold"),bg="white")
        year_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",10,"bold"),width=17,state="read only")
        year_combo["values"]=("Select Year","1st year","2nd year","3rd year","4th year")
        year_combo.current(0)
        year_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        # class student information
        class_student_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Class Student Informatiion",font=("times new roman",15,"bold"))
        class_student_frame.place(x=5,y=200 ,width=720,height=280)
        #Student name
        studentName_label=Label(class_student_frame,text="Student Name",font=("times new roman",13,"bold"),bg="white")
        studentName_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        studentName_entry=Entry(class_student_frame,textvariable=self.var_name,width=20,font=("times new roman",13,"bold"),bg="white")
        studentName_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        #roll number 
        student_roll_Number_label=Label(class_student_frame,text="Roll Number",font=("times new roman",13,"bold"),bg="white")
        student_roll_Number_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        student_roll_Number_entry=Entry(class_student_frame,textvariable=self.var_roll_num,width=20,font=("times new roman",13,"bold"),bg="white")
        student_roll_Number_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        #Gender 
        gender_label=Label(class_student_frame,text="Gender",font=("times new roman",13,"bold"),bg="white")
        gender_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        #gender_entry=Entry(class_student_frame,textvariable=self.var_gen,width=20,font=("times new roman",13,"bold"),bg="white")
        #gender_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gen,font=("times new roman",10,"bold"),width=17,state="read only")
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        #phon number
        phoneNumber_label=Label(class_student_frame,text="Phone Number",font=("times new roman",13,"bold"),bg="white")
        phoneNumber_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        phoneNumber_entry=Entry(class_student_frame,textvariable=self.var_phone_num,width=20,font=("times new roman",13,"bold"),bg="white")
        phoneNumber_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        #################################################
        # radio button
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=2,column=0)
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=2,column=2)
        ##buttton frames
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=10,y=120,width=700,height=100)
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
       
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=16,font=("times new roman",13,"bold"),bg="green",fg="white")
        update_btn.grid(row=0,column=1)
       
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=16,font=("times new roman",13,"bold"),bg="gray",fg="white")
        reset_btn.grid(row=0,column=2)
       
        delet_btn=Button(btn_frame,text="Delet",command=self.delete_data,width=16,font=("times new roman",13,"bold"),bg="red",fg="white")
        delet_btn.grid(row=0,column=3)
       
        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=10,y=155,width=700,height=100)
       
        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=33,font=("times new roman",13,"bold"),bg="yellow",fg="black")
        take_photo_btn.grid(row=0,column=0)
       
        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=33,font=("times new roman",13,"bold"),bg="yellow",fg="black")
        update_photo_btn.grid(row=0,column=1)
        #################################################
        ###RIGHT LABEL
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Detail",font=("times new roman",20,"bold"))
        Right_frame.place(x=750,y=10,width=730,height=580)

#*********** Searching System ***********#

        search_frame=LabelFrame(Right_frame,bd=2,relief=RIDGE,text="Searching System",font=("times new roman",15,"bold"))
        search_frame.place(x=5,y=150 ,width=720,height=80)

        searchBar_label=Label(search_frame,text="Search By: ",font=("times new roman",13,"bold"),bg="red", fg="white")
        searchBar_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",10,"bold"),width=17,state="readonly")
        search_combo["values"]=("Select ","Roll Number","Phone Number")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=Entry(search_frame,width=20,font=("times new roman",13,"bold"),bg="white")
        search_entry.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        search_btn=Button(search_frame,text="Search",width=13,font=("times new roman",12,"bold"),bg="gray",fg="white")
        search_btn.grid(row=0,column=3)

        showAll_btn=Button(search_frame,text="Show All",width=13,font=("times new roman",12,"bold"),bg="red",fg="white")
        showAll_btn.grid(row=0,column=4)

        #########Table Frame###################
        table_frame=Frame(Right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=5,y=240 ,width=720,height=300)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem","name","roll no","gen","phone no","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("roll no",text="Roll Number")
        self.student_table.heading("gen",text="Gender")
        self.student_table.heading("phone no",text="Phone")
        self.student_table.heading("photo",text="PhotoSample")
        self.student_table["show"]="headings"
        self.student_table.column("dep",width=90)
        self.student_table.column("course",width=80)
        self.student_table.column("year",width=90)
        self.student_table.column("sem",width=90)
        self.student_table.column("name",width=100)
        self.student_table.column("roll no",width=100)
        self.student_table.column("gen",width=70)
        self.student_table.column("phone no",width=100)
        self.student_table.column("photo",width=120)
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

############################### function decreatin #################

        # SAVE FUNCTION ******************
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()==""or self.var_roll_num.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="draj_desh",password="Top@12344321",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                    
                                                                    self.var_dep.get(),
                                                                    self.var_course.get(),
                                                                    self.var_year.get(),
                                                                    self.var_semester.get(),
                                                                    self.var_name.get(),
                                                                    self.var_roll_num.get(),
                                                                    self.var_gen.get(),
                                                                    self.var_phone_num.get(),
                                                                    self.var_radio1.get()

                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

#*************************** fetch data*******************
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="username",password="12345",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #=========================get cursor===============
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_name.set(data[4]),
        self.var_roll_num.set(data[5]),
        self.var_gen.set(data[6]),
        self.var_phone_num.set(data[7]),
        self.var_radio1.set(data[8])


        # update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()==""or self.var_roll_num.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to upadte this student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="username",password="12345",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("Update student set dep=%s,course=%s,year=%s,semester=%s,Name=%s,Roll=%s,Gender=%s,Phone=%s,Photo=%s where Roll=%s",(
                                                                                                                
                                                                    self.var_dep.get(),
                                                                    self.var_course.get(),
                                                                    self.var_year.get(),
                                                                    self.var_semester.get(),
                                                                    self.var_name.get(),
                                                                    self.var_roll_num.get(),
                                                                    self.var_gen.get(),
                                                                    self.var_phone_num.get(),
                                                                    self.var_radio1.get(),
                                                                    self.var_roll_num.get()

                                                                  ))
                else:
                     if not Update:
                         return
                messagebox.showinfo("Success","Student details successfully update completed",parent=self.root)
                conn.connect()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    ###********************** Delet Function *******

    def delete_data(self):
        if self.var_roll_num.get()=="":
            messagebox.showerror("Error","Student Roll must be required",parent=self.loop)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="username",password="12345",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where Roll=%s"
                    val=(self.var_roll_num.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


                ######### RESET function*****************
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_name.set("")
        self.var_roll_num.set("")
        self.var_gen.set("Select Gender")
        self.var_phone_num.set("")
        self.var_radio1.set("")

    ############ OpenCV #####

    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()==""or self.var_roll_num.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="username",password="12345",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.excute("select * from student")
                myresult=my_cursor.fetchhall()
                Roll=10
                for x in myresult:
                    Roll+1
                my_cursor.execute("Update student set dep=%s,course=%s,year=%s,semester=%s,Name=%s,Roll=%s,Gender=%s,Phone=%s,Photo=%s where Roll=%s",(
                                                                                                                
                                                                    self.var_dep.get(),
                                                                    self.var_course.get(),
                                                                    self.var_year.get(),
                                                                    self.var_semester.get(),
                                                                    self.var_name.get(),
                                                                    self.var_roll_num.get(),
                                                                    self.var_gen.get(),
                                                                    self.var_phone_num.get(),
                                                                    self.var_radio1.get(),
                                                                    self.var_roll_num.get()==Roll+1

                                                                  ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

             ###************* Load predefined data in face frontal from opencv**

                face_classfier=cv2.CascadClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classfier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #minimum neigbhour=5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_Roll=0
                while True: 
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_Roll+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(Roll)+"."+str(img_Roll)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_Roll),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitkey(1)==13 or int(img_Roll)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets compiled!!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

if __name__: "__main__"
root=Tk()
obj=Student(root)
root.mainloop()