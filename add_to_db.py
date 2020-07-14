#importing all modules
from tkinter import*
import sqlite3
import tkinter.messagebox

conn = sqlite3.connect('store.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS inventory(id INTEGER,name TEXT,stock INTEGER,cp INTEGER,sp INTEGER,totalcp INTEGER,totalsp INTEGER,vendor_name TEXT,vendor_no INTEGER,vendor_acc_no INTEGER)')
result=c.execute("SELECT Max(id) from inventory")
for r in result:
    id=r[0]
conn.commit()

class Database:
    def __init__(self,master,*args,**kwargs):
        self.master = master
        self.heading = Label(master, text="Add to the Database",font='arial 40 bold',fg='steelblue')
        self.heading.place(x=500,y=0)

        #labels for the window
        self.name_l = Label(master, text = "Enter Product Name",font="arial 18 bold")
        self.name_l.place(x=0,y=70)

        self.stock_l = Label(master, text = "Enter Stocks",font="arial 18 bold")
        self.stock_l.place(x=0,y=120)

        self.cp_l = Label(master, text = "Enter Cost Price",font="arial 18 bold")
        self.cp_l.place(x=0,y=170)

        self.sp_l = Label(master, text = "Enter Selling Price",font="arial 18 bold")
        self.sp_l.place(x=0,y=220)

        self.vendor_name_l = Label(master, text = "Enter vendor's name",font="arial 18 bold")
        self.vendor_name_l.place(x=0,y=270)

        self.vendor_no_l = Label(master, text = "Enter vendor's number",font="arial 18 bold")
        self.vendor_no_l.place(x=0,y=320)

        self.vendor_acc_no_l = Label(master, text = "Enter vendor's account number",font="arial 18 bold")
        self.vendor_acc_no_l.place(x=0,y=370)

        self.id_l = Label(master, text = "Enter ID",font="arial 18 bold")
        self.id_l.place(x=0,y=420)

        #entries for labels
        self.name_e = Entry(master,width=25,font="arial 18 bold")
        self.name_e.place(x=380,y=70)

        self.stock_e = Entry(master,width=25,font="arial 18 bold")
        self.stock_e.place(x=380,y=120)

        self.cp_e = Entry(master,width=25,font="arial 18 bold")
        self.cp_e.place(x=380,y=170)

        self.sp_e = Entry(master,width=25,font="arial 18 bold")
        self.sp_e.place(x=380,y=220)


        self.vendor_name_e = Entry(master,width=25,font="arial 18 bold")
        self.vendor_name_e.place(x=380,y=270)

        self.vendor_no_e = Entry(master,width=25,font="arial 18 bold")
        self.vendor_no_e.place(x=380,y=320)

        

        self.vendor_acc_no_e = Entry(master,width=25,font="arial 18 bold")
        self.vendor_acc_no_e.place(x=380,y=370)

        self.id_e = Entry(master,width=25,font='arial 18 bold')
        self.id_e.place(x=380,y=420)

        #button to add to the database
        self.btn_add = Button(master,text="Add to Database",width = "24",height = "2",bg="steelblue",fg="white",command=self.get_items)
        self.btn_add.place(x=530,y=470)

        #button to clear
        self.btn_clear = Button(master,text="Clear all fields",width=18,height=2,bg='lightgreen',fg='white',command=self.clear_all)
        self.btn_clear.place(x=380,y=470)

        #text box for logs
        self.tbox = Text(master,width="50",height="17")
        self.tbox.place(x=750,y=70)
        self.tbox.insert(END, "ID has reached upto: "+str(id))
    
    def get_items(self,*args,**kwargs):
        #get from entries
        self.name = self.name_e.get()
        self.stock = self.stock_e.get()
        self.cp = self.cp_e.get()
        self.sp = self.sp_e.get()
        self.vendor_name = self.vendor_name_e.get()
        self.vendor_no = self.vendor_no_e.get()
        self.vendor_acc_no = self.vendor_acc_no_e.get()

        if self.name==''or self.stock=='' or self.cp=='':
            tkinter.messagebox.showinfo("Error","Please fill all Entries.")
        #dynamic entries
        self.totalcp=float(self.cp)*float(self.stock)
        self.totalsp=float(self.sp)*float(self.stock)

        if self.name==''or self.stock=='' or self.cp==''or self.sp=='':
            tkinter.messagebox.showinfo("Error","Please fill all Entries.")
        else:
            sql="INSERT INTO inventory (name,stock,cp,sp,totalcp,totalsp,vendor_name,vendor_no,vendor_acc_no) values(?,?,?,?,?,?,?,?,?)"
            c.execute(sql,(self.name,self.stock,self.cp,self.sp,self.totalcp,self.totalsp,self.vendor_name,self.vendor_no,self.vendor_acc_no))
            conn.commit()
            #textbox insert
            tkinter.messagebox.showinfo("Great","successfully inserted")
            self.tbox.insert(END,"\n\nInserted "+str(self.name) + " into the database with code "+str(self.id_e.get()))
    def clear_all(self,*args,**kwargs):
        self.name_e.delete(0,END)
        self.stock_e.delete(0,END)
        self.cp_e.delete(0,END)
        self.sp_e.delete(0,END)
        self.vendor_name_e.delete(0,END)
        self.vendor_no_e.delete(0,END)
        self.vendor_acc_no_e.delete(0,END)
        self.id_e.delete(0,END)


root = Tk()
b = Database(root)
root.geometry("1366x768+0+0")
root.title("Add to the database")
root.mainloop()