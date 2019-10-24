import tkinter as t
import numpy as np
import pickle


class gui_hire:
    def __init__(self):
        self.m=t.Tk()
        self.m.title('Hired Or Not')
        self.m.geometry('500x650')
        self.gui()
        
    def gui(self):
        top = t.Frame(self.m,width=500,height=100,bg='#9ABCB8',relief=t.SUNKEN)
        top.pack(side=t.TOP)
        bot = t.Frame(self.m,width=500,height=500)
        bot.pack()
        self.last = t.Frame(self.m,width=500,height=150,bg='#DDE2E3')
        self.last.pack()
        
        labelinfo=t.Label(top,font=('arial',35,'bold'),text='Hired Or Not',bg='#9AACB8',bd=15)
        labelinfo.grid(row=0,column=0,ipadx=110)
        l1= t.Label(bot,text="Name",font=('arial',15,'bold'),bd=7);l2= t.Label(bot,text="Percentage",font=('arial',15,'bold'),bd=7);
        l3= t.Label(bot,text="BackLog",font=('arial',15,'bold'),bd=7);l4= t.Label(bot,text="Internship",font=('arial',15,'bold'),bd=7)
        l5= t.Label(bot,text="First Round",font=('arial',15,'bold'),bd=7);l6=t.Label(bot,text="Communication Skills",font=('arial',15,'bold'),bd=7)
        #Entry Box
        self.e1_val=t.StringVar();self.e2_val=t.StringVar();self.e3_val=t.StringVar();self.e4_val=t.StringVar();self.e5_val=t.StringVar();self.e6_val=t.StringVar()
        self.e1 = t.Entry(bot,textvariable=self.e1_val,font=('arial',15,'bold'),bd=7);self.e2 = t.Entry(bot,textvariable=self.e2_val,font=('arial',15,'bold'),bd=7)
        self.e3 = t.Entry(bot,textvariable=self.e3_val,font=('arial',15,'bold'),bd=7);self.e4 = t.Entry(bot,textvariable=self.e4_val,font=('arial',15,'bold'),bd=7)
        self.e5  = t.Entry(bot,textvariable=self.e5_val,font=('arial',15,'bold'),bd=7);self.e6 = t.Entry(bot,textvariable=self.e6_val,font=('arial',15,'bold'),bd=7)
        #Button
        b1= t.Button(self.last,text="Apply Linear Regression",height=1,width=20,command = self.calculateLinear,font=('arial',15,'bold'),bd=7)
        b2= t.Button(self.last,text="Apply Logistic Regression",height=1,width=20,command = self.calculateLogistic,font=('arial',15,'bold'),bd=7)            
        #grid
        l1.grid(row=1,column=0);self.e1.grid(row=1,column=1,padx=30,pady=10)
        l2.grid(row=2,column=0);self.e2.grid(row=2,column=1,padx=30,pady=10)
        l3.grid(row=3,column=0);self.e3.grid(row=3,column=1,padx=30,pady=10)
        l4.grid(row=4,column=0);self.e4.grid(row=4,column=1,padx=30,pady=10)
        l5.grid(row=5,column=0);self.e5.grid(row=5,column=1,padx=30,pady=10)   
        l6.grid(row=6,column=0);self.e6.grid(row=6,column=1,padx=30,pady=10)
        b1.grid(row=7,column=0,columnspan=1,pady=5,padx=120)
        b2.grid(row=8,column=0,columnspan=1,pady=3,padx=120)
        
        
        
        
    def calculateLinear(self):
        self.display('')
        model = pickle.load(open('models/linear.sav', 'rb'))
        predict = model.predict(self.prepare())
        if predict[0]==0:
            self.display('Not Hired')
        else:
            self.display('Hired')
        
    def calculateLogistic(self):
        self.display('')
        model = pickle.load(open('models/logistic.sav', 'rb'))
        predict = model.predict(self.prepare())
        if predict[0]==0:
            self.display('Not Hired')
        else:
            self.display('Hired')
    
    def display(self,output):
        l= t.Label(self.last,font=('arial',15,'bold'),bg='#687672',text=output,bd=10)
        l.grid(row=9,column=0,columnspan=1,pady=5,ipadx=80)
        
    
    def prepare(self):
        nx=np.array([int(self.e2_val.get()),int(self.e3_val.get()),int(self.e4_val.get()),int(self.e5_val.get()),int(self.e6_val.get())]).reshape(1,-1)
        return nx
    
gui = gui_hire()
gui.m.mainloop()      
