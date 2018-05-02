from tkinter import *
import random
import time;
import datetime
import tkinter.messagebox

root=Tk()


#############TITLE##################################
root.title("TOURISM IN INDIA")

root.configure(background="blue")

##########################################Frame definition###################################

Tops=Frame(root,width=100, height=30,bd=14)
Tops.pack(side=TOP, expand=True)

f1=Frame(root,width=100, height=100,bd=8)
f1.pack(side=LEFT,fill='both', expand=True)

f2=Frame(root,width=100, height=100,bd=8)
f2.pack(side=RIGHT,fill='both', expand=True)



Tops.configure(background="black")
f1.configure(background="blue")
f2.configure(background="red")

#canvas=Canvas(f1,bg="#016f89",width=100,height=100)
#canvas.pack()
#my_image=PhotoImage(file='C:\\Users\\savvy\\Desktop\\Monitor_India_Tourism_121')
#canvas.create_image(0,0,anchor=NW,image=my_image)

var1=StringVar()
var2=StringVar()
var3=StringVar()
var4=StringVar()
var5=StringVar()
var6=StringVar()

###########################Labels###################################


lblInfo=Label(Tops,font=("Helvetica", 40),text="TOURISM IN INDIA")
lblInfo.grid(row=0,column=0)



l2=Label(f1,text='ENTER TOURIST DETAILS :',font=("Helvetica", 30),width=25)
l2.grid(row=1,column=0,sticky=W)

l3=Label(f1,text='NAME',font=("Helvetica", 30),width=20)

l4=Label(f1,text='COUNTRY',font=("Helvetica", 30),width=20)
l5=Label(f1,text='DESTINATION',font=("Helvetica", 30),width=20)
l6=Label(f1,text='EMAIL',font=("Helvetica", 30),width=20)
l7=Label(f1,text='PASSPORT_ID',font=("Helvetica", 30),width=20)
l8=Label(f1,text='PASSPORT_ID',font=("Helvetica", 30),width=20)

var1=StringVar()
var2=StringVar()
var3=StringVar()
var4=StringVar()
var5=StringVar()
var6=StringVar()

####################################Entry Widget######################################################

e1=Entry(f1,textvariable=var1)
e2=Entry(f1,textvariable=var2)
e3=Entry(f1,textvariable=var3)
e4=Entry(f1,textvariable=var4)
e5=Entry(f1,textvariable=var5)
e6=Entry(f1,textvariable=var6)




l3.grid(row=2,column=0,sticky=W)
l4.grid(row=3,column=0,sticky=W)
l5.grid(row=4,column=0,sticky=W)
l6.grid(row=5,column=0,sticky=W)
l7.grid(row=6,column=0,sticky=W)


e1.grid(row=2,column=1)
e2.grid(row=3,column=1)
e3.grid(row=4,column=1)
e4.grid(row=5,column=1)
e5.grid(row=6,column=1)
e6.grid(row=7,column=1)
#################################BUTTON#######################################

b1=Button(f2,text='Next_Record',fg='red',font=("Helvetica", 20),width=20)
b1.grid(row=1,column=0)

b2=Button(f2,text='Add',fg='red',font=("Helvetica", 20),width=20)
b2.grid(row=2,column=0)

b3=Button(f2,text="First_Rec",fg='red',font=("Helvetica", 20),width=20)
b3.grid(row=3,column=0)

b4=Button(f2,text='Last_Rec',fg='red',font=("Helvetica", 20),width=20)
b4.grid(row=4,column=0)

b5=Button(f2,text='Search',fg='red',font=("Helvetica", 20),width=20)
b5.grid(row=5,column=0)

b7=Button(f2,text='Delete',fg='red',font=("Helvetica", 20),width=20)
b7.grid(row=6,column=0)

b8=Button(f2,text='Update',fg='red',font=("Helvetica", 20),width=20)
b8.grid(row=7,column=0)

count=0










#=====================================function Declaration===========================================================================




def error():
    var1.set("")
    var2.set("")
    var3.set("")
    var4.set("")
    var5.set("")
    l8=Label(f2,text='**Error**ALL FIELDS ARE NECESSARY')
    l8.grid(row=20,columns=3)



def  show(occur):
    data=open('m.txt','r')
    data_list=[]
    j=0
    var=data.readlines()
    for i in var:
        l=var[j].split()
        j+=1
        data_list.append(l)
    print(data_list)
    global count
    if count<=len(data_list)-1:
        var1.set(data_list[count][0])
        var2.set(data_list[count][1])
        var3.set(data_list[count][2])
        var4.set(data_list[count][3])
        var5.set(data_list[count][4])
        count+=1
        data.close()
    else:
        count=0


def record_added():
    l8=Label(f2,text='Record Added')
    l8.grid(row=20,columns=3)


    


def add(occur):
    data=open('m.txt','a')
    Name=var1.get()
    Country=var2.get()
    Destination=var3.get()
    Email=var4.get()
    Passport_id=var5.get()
    if Name=="" or Country=="" or Destination=="" or Email=="" or Passport_id=="" :
        error()
    else:
        
        for i in range(len(Name),14):
            Name=Name+" "
        for i in range(len(Country),15):
            Country=Country+" "
        for i in range(len(Destination),14):
            Destination=Destination+" "
        for i in range(len(Email),14):
            Email=Email+" "
        for i in range(len(Passport_id),14):
            Passport_id=Passport_id+" "
        
        data.writelines(Name+"  "+Country+" "+Destination+" "+Email+" "+" "+Passport_id+'\n')
        var1.set("")
        var2.set("")
        var3.set("")
        var4.set("")
        var5.set("")
        record_added()
    data.close()




def show_first(occur):
    import re
    data=open('m.txt','r')
    var=data.readline()
    string=re.sub(' +',' ',var)
    l=string.split()
    var1.set(l[0])
    var2.set(l[1])
    var3.set(l[2])
    var4.set(l[3])
    var5.set(l[4])
    data.close()
    




def show_last(occur):
    data=open('m.txt','r')
    for i in data:
        var=i
    string=re.sub(' +',' ',var)
    l=string.split()
    var1.set(l[0])
    var2.set(l[1])
    var3.set(l[2])
    var4.set(l[3])
    var5.set(l[4])
    data.close()




def ok(occur):
    import re
    flag=1
    data=open('m.txt','r')
    idi = e6.get()
    for i in data:
        var=i
        string=re.sub(' +',' ',var)
        l=string.split()
        if idi==l[4]:
            var1.set(l[0])
            var2.set(l[1])
            var3.set(l[2])
            var4.set(l[3])
            var5.set(l[4])
            flag=1
            break
        else:
            flag=0
            pass
    if flag==0:
        var1.set("")
        var2.set("")
        var3.set("")
        var4.set("")
        var5.set("")
    data.close()


    

def delete(occur):
    data=open('m.txt','r')
    idi=var6.get()
    data_list=[]
    j=0
    var=data.readlines()
    for i in var:
        l=var[j].split()
        j+=1
        data_list.append(l)
    print(data_list)
    data.close()
    data=open('m.txt','w')
    for i in range(0,len(data_list)):
        if idi!=data_list[i][4]:
            Name=data_list[i][0]
            Country=data_list[i][1]
            Destination=data_list[i][2]
            Email=data_list[i][3]
            Passport_id=data_list[i][4]
            
            for i in range(len(Name),14):
                Name=Name+" "
            for i in range(len(Country),15):
                Country=Country+" "
            for i in range(len(Destination),14):
                Destination=Destination+" "
            for i in range(len(Email),14):
                Email=Email+" "
            for i in range(len(Passport_id),14):
                Passport_id=Passport_id+" "
            
            data.writelines(Name+"  "+Country+" "+Destination+" "+Email+" "+" "+Passport_id+'\n')
        else:
            pass
    var1.set("")
    var2.set("")
    var3.set("")
    var4.set("")
    var5.set("")
    data.close()  


def search(occur):
    l8.grid(row=10,column=0)
    e6.grid(row=10,column=1)
    b5.bind('<Button-1>',ok)
    b7.bind('<Button-1>',delete)
    
    
####################################Button#########################################################################################################################################    
b1.bind('<Button-1>',show)
b2.bind('<Button-1>',add)
b3.bind('<Button-1>',show_first)
b4.bind('<Button-1>',show_last)
b5.bind('<Button-1>',search)
b7.bind('<Button-1>',search)
b8.bind('<Button-1>',search)    

    

root.mainloop()
