from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import mysql.connector

class User_Register:
    def __init__(self,root):
        self.root = root
        self.root.title('Inventory Management')
        self.root.geometry("1600x800")
        self.root.iconbitmap('C:/Users/Niranjan Khedkar/OneDrive/Desktop/Stock-Management-System-master/inventory/button images(login)/Iconinv.ico')

                      ##DESIGN#######  

        self.bg= ImageTk.PhotoImage(Image.open("C:/Users/Niranjan Khedkar/OneDrive/Desktop/Stock-Management-System-master/inventory/button images(login)/bglogin.jpg"))
        bg= Label(self.root,image=self.bg)
        bg.place(x=0,y=0,relwidth=1,relheight=1)
        self.login_b=ImageTk.PhotoImage(Image.open("C:/Users/Niranjan Khedkar/OneDrive/Desktop/Stock-Management-System-master/inventory/button images(login)/button_login (2).png"))
        log_btn=Label(self.root,image=self.login_b)
        log_btn.place(x=175, y=550, height = 68, width = 250)
        self.regs_b=ImageTk.PhotoImage(Image.open("C:/Users/Niranjan Khedkar/OneDrive/Desktop/Stock-Management-System-master/inventory/button images(login)/button_register.png"))
        #reg_btn=Label(self.root,image=self.reg_btn)
        #reg_btn.place(x=175, y=400, height = 75, width = 300)
        def back():

            self.root.destroy()
            import startpage


        def login():
            self.root.destroy()
            import startpage

        def unew_login():
            if self.usrnew_1sten.get() =="" or self.usrnew_lasten.get()=="" or self.usrnew_iden.get()=="" or self.answeren.get()=="" or self.usrnew_passen.get()=="" or self.usrnew_passcnen.get()=="":
                messagebox.showerror("Error","All fields are mandatory",parent = self.root)
            elif self.usrnew_passen.get() != self.usrnew_passcnen.get():
                messagebox.showerror("Error","Password does not match",parent = self.root)
            else:
                try:
                    con = mysql.connector.connect(host="localhost",user="root",passwd="",database="Inventory")
                    cur = con.cursor(buffered=True)
                    select = "SELECT mail_id FROM USERS"
                    cur.execute(select)
                    for (mail_id) in cur:
                        if self.usrnew_iden.get() == mail_id:
                            messagebox.showerror("Error","User already exists",parent = self.root)
                        else:
                            login_insert = "INSERT INTO users (f_name , l_name, mail_id , que , answer , password) VALUES (%s, %s, %s, %s, %s, %s)"
                            keys = (self.usrnew_1sten.get(),
                                    self.usrnew_lasten.get(),
                                    self.usrnew_iden.get(),
                                    self.security_combo.get(),
                                    self.answeren.get(),
                                    self.usrnew_passen.get()
                                    )
                            cur.execute(login_insert,keys)
                            con.commit()
                            con.close()
                            messagebox.showinfo("Success","Registration successful",parent = self.root)
                except Exception as es:
                    messagebox.showerror("Error",f"Error due to {es}",parent = self.root)
                self.root.destroy()
                import startpage                                     


        self.usrn_frame = LabelFrame(self.root, text ="SIGN UP", padx = 10, pady = 10, font =("Arial",20),bg="Orange")
        self.usrn_frame.place(x=650, y=125, height = 550, width = 700)
        usrnew_1st = Label(self.usrn_frame, text = "First Name     : ",font =("Arial",16),bg="Orange").grid(row = 1, column = 0, padx = 10, pady = 10)
        self.usrnew_1sten = Entry(self.usrn_frame, width = 40, font =("Arial",16))
        self.usrnew_1sten.grid(row = 1, column = 1, padx = 10, pady = 10)
        usrnew_last = Label(self.usrn_frame, text = "Last Name     : ",font =("Arial",16),bg="Orange").grid(row = 2, column = 0, padx = 10, pady = 10)
        self.usrnew_lasten = Entry(self.usrn_frame, width = 40, font =("Arial",16))
        self.usrnew_lasten.grid(row = 2, column = 1, padx = 10, pady = 10)
        usrnew_id = Label(self.usrn_frame, text = "E-mail id        : ", font =("Arial",16),bg="Orange").grid(row = 3, column = 0, padx = 10, pady = 10)
        self.usrnew_iden = Entry(self.usrn_frame, width = 40, font =("Arial",16))
        self.usrnew_iden.grid(row = 3, column = 1, padx = 10, pady = 10)
        usrnew_pass = Label(self.usrn_frame, text = "Password      : ", font =("Arial",16),bg="Orange").grid(row = 6, column = 0, padx = 10, pady = 10)
        self.usrnew_passen = Entry(self.usrn_frame,show = "*", width = 40, font =("Arial",16))
        self.usrnew_passen.grid(row = 6, column = 1, padx = 10, pady = 10)
        security = Label(self.usrn_frame, text = "Security Que : ", font =("Arial",16),bg="Orange").grid(row = 4, column = 0, padx = 10, pady = 10)
        self.security_combo = ttk.Combobox(self.usrn_frame, font =("Arial",16), state = "readonly" , width = 39, justify = "center")
        self.security_combo['values']=("Select","Your favourite book","Your favourite movie","Your best friend")
        self.security_combo.grid(row = 4, column = 1, padx = 10, pady = 10 )
        self.security_combo.current(0)
        answer = Label(self.usrn_frame, text = "Answer         : ", font =("Arial",16),bg="Orange").grid(row = 5, column = 0, padx = 10, pady = 10)
        self.answeren = Entry(self.usrn_frame, width = 40, font =("Arial",16))
        self.answeren.grid(row = 5, column = 1, padx = 10, pady = 10)
        usrnew_passcn = Label(self.usrn_frame, text = "Confirm Pass : ", font =("Arial",16),bg="Orange").grid(row = 7, column = 0, padx = 10, pady = 10)
        self.usrnew_passcnen = Entry(self.usrn_frame,show = "*", width = 40, font =("Arial",16))
        self.usrnew_passcnen.grid(row = 7, column = 1, padx = 10, pady = 10)
        self.usrreg_login = Button (self.usrn_frame, image=self.regs_b, command = unew_login, font = ("Arial",18) )
        self.usrreg_login.place(x=175, y=400, height = 75, width = 300)
        self.signup = Button(self.root, image=self.login_b, command = login, font = ("Arial",18) )
        self.signup.place(x=175, y=550, height = 68, width = 250)
        self.back_btn = Button(self.root, text  = "<BACK", font =("Arial",18),bd="0",bg="Light Blue",fg="RED", command= back)
        self.back_btn.grid(row=0, column=0)
        
root = Tk()
obj = User_Register(root)
root.mainloop()
