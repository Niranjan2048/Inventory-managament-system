from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox
from PIL import Image,ImageTk
import math,random



class Customer:
    def __init__(self,root,id):
        self.root = root
        self.root.title("----INVENTORY MANAGEMENT----")
        self.root.geometry("1600x800+0+0")
        self.root.iconbitmap('C:/Users/Niranjan Khedkar/OneDrive/Desktop/Stock-Management-System-master/inventory/button images(login)/Iconinv.ico')
        bg_color="Royalblue3"
        bg_titlecolor="navy"
        title=Label(self.root,text="INVENTORY MANAGEMENT",bd=10,relief=SOLID,fg="WHITE",bg=bg_titlecolor,font=("times new roman",40,"bold"))
        title.pack(side=TOP,fill=X)
        
        
        #-----------------variables---------
        self.product_id=StringVar()
        self.product_name=StringVar()
        self.product_qty=IntVar()
        self.search_by=StringVar()
        self.search_txt=StringVar()
        self.product_price=IntVar()
        self.user_id = StringVar()
        self.product_id.set(str(random.randint(1000,9999)))
        

       #----------MANAGE FRAME----------
        
        self.manage_frame=Frame(self.root,bd=5,relief=RIDGE,bg=bg_color)
        self.manage_frame.place(x=20,y=100,width=600,height=650)
        m_title=Label(self.manage_frame,text="PRODUCT MANAGEMENT",bg=bg_color,fg="black",font=("times new roman",20,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_id=Label(self.manage_frame,text="USER ID",bg=bg_color,fg="black",font=("times new roman",16,"bold"))
        lbl_id.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        self.txt_id=Entry(self.manage_frame,textvariable=self.user_id,font=("times new roman",16,"bold"),bd=5,relief=GROOVE,state=DISABLED)
        self.user_id.set(id)
        self.txt_id.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        lbl_id=Label(self.manage_frame,text="PRODUCT ID",bg=bg_color,fg="black",font=("times new roman",16,"bold"))
        lbl_id.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        self.txt_id=Entry(self.manage_frame,textvariable=self.product_id,font=("times new roman",16,"bold"),bd=5,relief=GROOVE)
        self.txt_id.grid(row=2,column=1,pady=10,padx=20,sticky="w")
        
        lbl_name=Label(self.manage_frame,text="PRODUCT NAME",bg=bg_color,fg="black",font=("times new roman",16,"bold"))
        lbl_name.grid(row=3,column=0,pady=10,padx=20,sticky="w")

        self.txt_name=Entry(self.manage_frame,textvariable=self.product_name,font=("times new roman",16,"bold"),bd=5,relief=GROOVE)
        self.txt_name.grid(row=3,column=1,pady=10,padx=20,sticky="w")
        
        lbl_qty=Label(self.manage_frame,text=" QUANTITY",bg=bg_color,fg="black",font=("times new roman",16,"bold"))
        lbl_qty.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        self.txt_qty=Entry(self.manage_frame,textvariable=self.product_qty,font=("times new roman",16,"bold"),bd=5,relief=GROOVE)
        self.txt_qty.grid(row=4,column=1,pady=10,padx=20,sticky="w")
        
        lbl_price=Label(self.manage_frame,text="PRICE (PER UNIT)",bg=bg_color,fg="black",font=("times new roman",16,"bold"))
        lbl_price.grid(row=5,column=0,pady=10,padx=20,sticky="w")

        self.txt_price=Entry(self.manage_frame,textvariable=self.product_price,font=("times new roman",16,"bold"),bd=5,relief=GROOVE)
        self.txt_price.grid(row=5,column=1,pady=10,padx=20,sticky="w")


        #-----------ALL IMAGES--------------
        self.search_b1=ImageTk.PhotoImage(file="C:/Users/Niranjan Khedkar/OneDrive/Desktop/Stock-Management-System-master/inventory/button_images/search1.png")
        self.add_b1=ImageTk.PhotoImage(file="C:/Users/Niranjan Khedkar/OneDrive/Desktop/Stock-Management-System-master/inventory/button_images/add2.png")
        self.update_b1=ImageTk.PhotoImage(file="C:/Users/Niranjan Khedkar/OneDrive/Desktop/Stock-Management-System-master/inventory/button_images/update1.png")
        self.delete_b1=ImageTk.PhotoImage(file="C:/Users/Niranjan Khedkar/OneDrive/Desktop/Stock-Management-System-master/inventory/button_images/remove.png")
        self.clear_b1=ImageTk.PhotoImage(file="C:/Users/Niranjan Khedkar/OneDrive/Desktop/Stock-Management-System-master/inventory/button_images/clear2.png")
        self.show_b1=ImageTk.PhotoImage(file="C:/Users/Niranjan Khedkar/OneDrive/Desktop/Stock-Management-System-master/inventory/button_images/show1.png")
        self.exit_b=ImageTk.PhotoImage(file="C:/Users/Niranjan Khedkar/OneDrive/Desktop/Stock-Management-System-master/inventory/button_images/exit.png")
        #----------BUTTON FRAME----------
        self.btn_frame=Frame(self.manage_frame,bd=5,relief=GROOVE,bg=bg_color)
        self.btn_frame.place(x=20,y=450,width=440)

        add_btn=Button(self.btn_frame,image=self.add_b1,width=85,height=35,bg=bg_color,bd=0,command=self.add_product).grid(row=0,column=0,padx=10,pady=10)
        update_btn=Button(self.btn_frame,image=self.update_b1,width=85,height=35,bg=bg_color,bd=0,command=self.update_data).grid(row=0,column=1,padx=10,pady=10)
        delete_btn=Button(self.btn_frame,image=self.delete_b1,width=85,height=35,bg=bg_color,bd=0,command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
        clear_btn=Button(self.btn_frame,image=self.clear_b1,width=85,height=35,bg=bg_color,bd=0,command=self.clear).grid(row=0,column=3,padx=10,pady=10)
        Exit_btn=Button(self.manage_frame,image=self.exit_b,command=self.Window_Exit,width=88,height=70,text="LOGOUT",font=("Arial",7,"bold"),compound=TOP,pady=6,bg="snow2",fg="black",bd=5)
        Exit_btn.place(x=200,y=540)
          
          
         #----------DETAILS FRAME----------
        self.details_frame=Frame(self.root,bd=5,relief=RIDGE,bg=bg_color)
        self.details_frame.place(x=640,y=100,width=850,height=650)
        
        lbl_search=Label(self.details_frame,text="SEARCH BY",bg=bg_color,fg="black",font=("times new roman",16,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        combo_search=ttk.Combobox(self.details_frame,textvariable=self.search_by,font=("times new roman",13),state='readonly',width=10)
        combo_search['values']=("product_name","product_id")
        combo_search.grid(row=0,column=1,padx=20,pady=10)

        self.txt_search=Entry(self.details_frame,width=15,textvariable=self.search_txt,font=("times new roman",16,"bold"),bd=5,relief=GROOVE)
        self.txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")
        
        search_btn=Button(self.details_frame,image=self.search_b1,text="SEARCH",width=90,height=30,bd=0,bg=bg_color,command=self.search_data).grid(row=0,column=3,padx=10,pady=10)
        showall_btn=Button(self.details_frame,image=self.show_b1,width=90,height=30,bg=bg_color,bd=0,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)

        #-----------table frame---------
        self.table_frame=Frame(self.details_frame,bd=4,relief=RIDGE,bg=bg_color)
        self.table_frame.place(x=10,y=70,width=800,height=540)
        
        
        scroll_x=Scrollbar(self.table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(self.table_frame,orient=VERTICAL)
        self.invent_table=ttk.Treeview(self.table_frame,columns=("PRODUCT ID","PRODUCT NAME","QUANTITY","PRICE","TOTAL"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.invent_table.xview)
        scroll_y.config(command=self.invent_table.yview)
        self.invent_table.heading("PRODUCT ID",text="PRODUCT ID:")
        self.invent_table.heading("PRODUCT NAME",text="PRODUCT NAME:")
        self.invent_table.heading("QUANTITY",text="QUANTITY:")
        self.invent_table.heading("PRICE",text="PRICE:")
        self.invent_table.heading("TOTAL",text="TOTAL:")
        self.invent_table['show']='headings'
        self.invent_table.column("PRODUCT ID",width=70)
        self.invent_table.column("PRODUCT NAME",width=200)
        self.invent_table.column("QUANTITY",width=150)
        self.invent_table.column("PRICE",width=150)
        self.invent_table.column("TOTAL",width=150)

        self.invent_table.pack(fill=BOTH,expand=1)
        self.invent_table.bind("<ButtonRelease-1>",self.get_cursor)
        
        self.fetch_data()
    
    def Window_Exit(self):
        mes= messagebox.askyesno("Notification","Do You want to logout?")    
        if mes > 0:
            self.root.destroy()
            import startpage
    def add_product(self):
        if self.product_id.get()=="" or self.product_name.get()=="":
            messagebox.showerror("Error","All fields arer required!!")
        else:
            self.total = float(self.product_qty.get())*float(self.product_price.get())

        con=pymysql.connect(host="localhost",user="root",password="",database="inventory")
        cur=con.cursor()
        cur.execute("insert into inventory values(%s,%s,%s,%s,%s,%s)",(self.user_id.get(),self.product_id.get(),self.product_name.get(),self.product_qty.get(),self.product_price.get(),self.total))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        messagebox.showinfo("success","record has been inserted",parent = self.root)

    
    def fetch_data(self): 
        con=pymysql.connect(host="localhost",user="root",password="",database="inventory")
        cur=con.cursor()
        cur.execute("select product_id,product_name,product_qty,product_price,total from inventory")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.invent_table.delete(*self.invent_table.get_children())
            for row in rows:
                self.invent_table.insert('',END,values=row)
                con.commit()
        con.close()

    
    def clear(self):
        self.product_id.set(str(random.randint(1000,9999)))
        self.product_name.set("")
        self.product_qty.set("")  
        self.product_price.set("") 

    
    def get_cursor(self,ev):
        cursor_row=self.invent_table.focus()
        content=self.invent_table.item(cursor_row)
        row=content['values']
        self.product_id.set(row[0])
        self.product_name.set(row[1])
        self.product_qty.set(row[2])
        self.product_price.set(row[3]) 
        
        
    def update_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="inventory")
        cur=con.cursor()
        cur.execute("update inventory set product_name=%s,product_qty=%s,product_price=%s where product_id=%s",(self.product_name.get(),self.product_qty.get(),self.product_price.get(),self.product_id.get()))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
    
    
    def delete_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="inventory")
        cur=con.cursor()
        cur.execute("delete  from inventory where product_id=%s",self.product_id.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
    
    
    def search_data(self): 
        con=pymysql.connect(host="localhost",user="root",password="",database="inventory")
        cur=con.cursor()
        if f'{self.search_by.get()}'=='product_id':
            statement=f"select product_id,product_name,product_qty,product_price,total from inventory where product_id='{self.search_txt.get()}'"
        else:
            statement=f"select product_id,product_name,product_qty,product_price,total from inventory where product_name='{self.search_txt.get()}'"
        cur.execute(statement)
        self.invent_table.delete(*self.invent_table.get_children())
        rows=cur.fetchall()
        if len(rows)!=0:
            self.invent_table.delete(*self.invent_table.get_children())
            for row in rows:
                self.invent_table.insert('',END, values=row)
            con.commit()
        con.close()


def run_supplier(id):
    root=Tk() 
    obj=Customer(root,id)
    print(id)
    root.mainloop()
