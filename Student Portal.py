from tkinter import *
from tkinter import ttk
import random as r
import mysql.connector as c
from datetime import *

h=c.connect(host='localhost',user='root',passwd='nani4',database='himanshu')
k=h.cursor()
if h.is_connected()==1:
    print('connected')
else:
    print('not connected')


def pchk(uname,pwd):
        k.execute("select * from klu where name like '%"+uname+"%' and password='"+pwd+"' and regno ='"+pwd[:-2]+"'")
        global fet
        fet=k.fetchone()        
        if uname=='admin' and pwd=='ad10':
            return 1
        elif fet!=[] and fet[1]==pwd[:-2] and fet[15]==pwd:
            return 1
        else:
            return 0

def sign_up():
        usname1=en1.get()
        regno1=en2.get()
        paswd1=regno1+chr(r.randint(65,90))+chr(r.randint(65,90))#+str(r.randint(0,9))+str(r.randint(0,9))
        k.execute("select regno,name,password from klu where name like '%"+usname1+"%' and Regno='"+regno1+"'")
        ft=k.fetchall()
        if usname1=='' or regno1=='' or len(regno1) not in [10,11] or regno1.isdigit()==0 :
                Label(win2,text=' '*100,bg='#9fe6e8').place(y=350+10,x=250+100)
                Label(win2,text='Invalid username or registration No.',font=('constantia',12),bg='#9fe6e8',fg='red').place(y=350+10,x=250+100)
        elif ft[0][-1]!=None:
                Label(win2,text=' '*100,bg='#9fe6e8').place(y=350+10,x=250+100)
                Label(win2,text='Already Exist'+' '*20,font=('constantia',12),bg='#9fe6e8',fg='red').place(y=350+10,x=250+180)
        elif ft[0][0]==regno1 and ft[0][-1]==None:
                k.execute("update klu set password='"+paswd1+"' where regno='"+regno1+"'")
                h.commit()
                Label(win2,text=' '*100,bg='#9fe6e8').place(y=350+10,x=250+100)
                Label(win2,text=usname1+' your password created successfully',font=('constantia',13),fg='#09ad0c',bg='#9fe6e8').place(y=350+10,x=250+100)
                Label(win2,text=paswd1,font=('Comic Sans MS',11),fg='#f58c8c',bg='#9fe6e8').place(y=380+10,x=300+100)
                bt1.config(state=DISABLED)
                Button(win2,text=' Next ',command=signin,padx=5,pady=5,bd=0).place(x=350+100,y=440)
        else:
                Label(win2,text=' '*100,bg='#9fe6e8').place(y=350+10,x=250+100)
                Label(win2,text='ERROR',bg='#9fe6e8').place(y=350+10,x=250+160)
                
        
def sign_in():
    usname2=en1.get()
    paswd2=en2.get()
    if pchk(usname2,paswd2)==1 :
        Label(win1,text=' '*100,bg='#9fe6e8').place(y=350+10,x=200+100)
        Label(win1,text='Sign In Successful',font=('constantia',13),fg='#09ad0c',bg='#9fe6e8').place(y=350+10,x=300+100)
        bt2.config(state=DISABLED)
        Button(win1,text=' Next ',command=home,padx=5,pady=5,bd=0).place(x=350+100,y=420)
    elif usname2=='' or paswd2=='' or len(paswd2) not in [12,13] or paswd2.isalnum()==0 or pchk(usname2,paswd2)==0:
        Label(win1,text='Invalid username or password',font=('constantia',12),fg='red',bg='#9fe6e8').place(y=350+10,x=250+100)


def signup():
    global win2
    win2=Tk()#Toplevel(win)
    win2.title('sign up')
    win2.geometry('1000x600')
    win2.resizable(0,0)
    win2.config(bg='#9fe6e8')
    Exit()
    global cls
    cls=3
    Label(win2,text='Sign Up',font=('constantia',40),fg='#5632a8',bg='#9fe6e8').place(x=285+100,y=120)
    global en1
    Label(win2,text='Username',font=('constantia',10),bg='#9fe6e8').place(y=210+20,x=160+100)
    en1=Entry(win2,font=('cambria',20),bg='#f5edda')
    en1.place(x=230+100,y=200+20)
    global en2
    Label(win2,text='Reg no.',font=('constantia',10),bg='#9fe6e8').place(y=260+20,x=170+100)
    en2=Entry(win2,font=('cambria',20),bg='#f5edda')
    en2.place(x=230+100,y=250+20)
    global bt1
    bt1=Button(win2,text=' Sign Up',command=sign_up,fg='#f2f1e1',bg='#2ebf17',width=15,padx=10,pady=5,bd=0)
    bt1.place(x=310+100,y=300+20)
    Button(win2,text=' Exit ',command=Exit,padx=10,pady=5,bd=0).place(x=2,y=2)
    Button(win2,text=' sign in ',command=signin,padx=10,pady=5,bd=0).place(x=930,y=2)
    Label(win2,text=str(datetime.now().date()),font=('times',12),fg='blue',bg='#9fe6e8').place(x=900,y=540)
    Label(win2,text=str(datetime.now().time())[:-10],font=('times',12),fg='blue',bg='#9fe6e8').place(x=900,y=560)

def signin():
    global win1
    win1=Tk()#Toplevel(win)
    win1.title('sign in')
    win1.geometry('1000x600')
    win1.resizable(0,0)
    win1.config(bg='#9fe6e8')
    Exit()
    global cls
    cls=2
    Label(win1,text='Sign In',font=('constantia',40),fg='#5632a8',bg='#9fe6e8').place(x=285+100,y=120)
    global en1
    Label(win1,text='Username',font=('constantia',10),bg='#9fe6e8').place(y=210+20,x=160+100)
    en1=Entry(win1,font=('cambria',20),bg='#f5edda')
    en1.place(x=230+100,y=200+20)
    global en2
    Label(win1,text='Password',font=('constantia',10),bg='#9fe6e8').place(y=260+20,x=160+100)
    en2=Entry(win1,font=('cambria',20),bg='#f5edda',show='*')
    en2.place(x=230+100,y=250+20)
    global bt2
    bt2=Button(win1,text=' Sign In ',command=sign_in,fg='#f2f1e1',bg='#2ebf17',width=15,padx=10,pady=5,bd=0)
    bt2.place(x=310+100,y=300+20)
    Button(win1,text=' Exit ',command=Exit,padx=10,pady=5,bd=0).place(x=2,y=2)
    Button(win1,text=' sign up ',command=signup,padx=10,pady=5,bd=0).place(x=925,y=2)
    Label(win1,text=str(datetime.now().date()),font=('times',12),fg='blue',bg='#9fe6e8').place(x=900,y=540)
    Label(win1,text=str(datetime.now().time())[:-10],font=('times',12),fg='blue',bg='#9fe6e8').place(x=900,y=560)

def Exit():
    if cls==1:
        win.destroy()#win.withdraw()
    elif cls==2:
        win1.destroy()
    elif cls==3:
        win2.destroy()
    elif cls==4:
        f1.destroy()
    elif cls==5:
        f2.destroy()
    elif cls==6:
        f3.destroy()
    elif cls==7:
        f4.destroy()
    elif cls==8:
        f5.destroy()
    elif cls==9:
        f6.destroy()
    else:
        pass
    
def signout():
    win3.destroy()
    global cls
    cls=0
    Main()

def Main():
    global win
    win=Tk()
    win.title('Student portal')
    win.geometry('1000x600')
    win.resizable(0,0)
    win.config(bg='#9fe6e8')
    Exit()
    global cls
    cls=1
    Label(win,text='STUDENT PORTAL',font=('Georgia',40),fg='black',bg='#9fe6e8').place(x=250,y=40)
    Label(win,text='Sign Up'+(' '*13)+'Sign In',font=('Georgia',30),fg='#5632a8',bg='#9fe6e8').place(x=150+130,y=180)
    Label(win,text='Are you new?',font=('constantia',12),bg='#9fe6e8').place(x=170+130,y=250)
    Label(win,text='Already created?',font=('constantia',12),bg='#9fe6e8').place(x=420+130,y=250)
    Button(win,text=' Sign Up ',command=signup,padx=10,pady=5,bd=0).place(x=180+130,y=290)
    Button(win,text=' Sign In ',command=signin,padx=10,pady=5,bd=0).place(x=450+130,y=290)
    Button(win,text=' Exit ',command=Exit,padx=10,pady=5,bd=0).place(x=2,y=2)
    Label(win,text=str(datetime.now().date()),font=('times',12),fg='blue',bg='#9fe6e8').place(x=900,y=540)
    Label(win,text=str(datetime.now().time())[:-10],font=('times',12),fg='blue',bg='#9fe6e8').place(x=900,y=560)

    
def details():
    global f2
    f2=Frame(win3,bg='#f2f1e1',width=720,height=530,highlightthickness=1,highlightbackground='black')
    f2.place(x=250,y=50)
    Exit()
    global cls
    cls=5
    Label(f2,text=' Personal Details ',font=('times',15),fg='red',bg='#f2f1e1').place(x=250,y=30)
    for a in range(12):
        tle=['Name','Reg No.','Degree','Course','Stream','Semester','Section','DOB','Father Name','Mother Name','Phone','Address']
        yc=[40,70,100,130,160,190,220,250,280,310,340,370]
        Label(f2,text=tle[a],font=('times',13),bg='#f2f1e1').place(x=130,y=yc[a]+40)

    for b in yc:
        Label(f2,text=':',font=('calibri',14),bg='#f2f1e1').place(x=240,y=b+40)
        
    for c in range(12):
        dtl=[fet[2],fet[1],'B Tech',fet[4],fet[5],'I',fet[3],fet[6],fet[7],fet[8],fet[9],fet[10]]
        Label(f2,text=dtl[c],font=('times',14),bg='#f2f1e1').place(x=280,y=yc[c]+40)
    Label(f2,text='To update the datails ?',font=('times',10),bg='#f2f1e1').place(x=200,y=500)
    Button(f2,text='click here',font=('times',10),fg='blue',bg='#f2f1e1',command=updatedtls,border=0).place(x=330,y=500)


def updatedtls():
    global f6
    f6=Frame(win3,bg='#f2f1e1',width=720,height=530,highlightthickness=1,highlightbackground='black')
    f6.place(x=250,y=50)
    Exit()
    global cls
    cls=9
    Label(f6,text='Details Updation',font=('times',16),fg='red',bg='#f2f1e1').place(x=300,y=50)
    global cmb
    val=['Stream','DOB','Father_name','Mother_name','Contact','Address']
    cmb=ttk.Combobox(f6,values=val,state='readonly',font=('times',13))
    cmb.place(x=200,y=130)
    cmb.set('select to update')

    def updtls():
        #en3['state']=DISABLED
        bt3['state']=DISABLED
        k.execute("update klu set "+e+"='"+en3.get()+"' where regno='"+fet[1]+"'")
        h.commit()
        Label(f6,text='Update successful',font=('times',12),fg='green',bg='#f2f1e1').place(x=270,y=360)
    def seldtls():
        global e
        for e in val:
            if cmb.get()==e:
                Label(f6,text='Update '+e+' '*20,font=('times',12),bg='#f2f1e1').place(x=100,y=250)
                global en3
                en3=Entry(f6,font=('cambria',14),bd=1,width=50)
                en3.place(x=100,y=280)
                global bt3
                bt3=Button(f6,text=' Update ',font=('times',12),command=updtls,bd=0,bg='light pink')
                bt3.place(x=300,y=320)
                Label(f6,text=' '*30,font=('times',12),bg='#f2f1e1').place(x=260,y=360)
                break
    Button(f6,text=' Next ',font=('times',12),command=seldtls,bd=1).place(x=450,y=130)

def fees():
    global f3
    f3=Frame(win3,bg='#f2f1e1',width=720,height=530,highlightthickness=1,highlightbackground='black')
    f3.place(x=250,y=50)
    Exit()
    global cls
    cls=6
    Label(f3,text='Fee Details',font=('times',15),fg='red',bg='#f2f1e1').place(x=300,y=60)
    f31=Frame(f3,width=0)
    f31.place(x=50,y=150)
    
    tbl=ttk.Treeview(f31,column=('c1','c2','c3','c4','c5'),show='headings',height=5)
    for d,e,f in [('#1',50,'Sno'),('#2',200,'Fee Type'),('#3',120,'Total Fee'),('#4',120,'Fee paid'),('#5',120,'Fee Due')]:
            tbl.column(d,anchor=CENTER,width=e)
            tbl.heading(d,text=f)
            
    tbl.insert('','end',text='',values=(1,'Admission Fee',10000,10000,0))
    tbl.insert('','end',text='',values=(2,'Semester Fee',fet[11],fet[12],fet[11]-fet[12]))
    tbl.pack()

def exams():
    global f4
    f4=Frame(win3,bg='#f2f1e1',width=720,height=530,highlightthickness=1,highlightbackground='black')
    f4.place(x=250,y=50)
    Exit()
    cls=7
    Label(f4,text=' Exams ',font=('times',15),fg='red',bg='#f2f1e1').place(x=300,y=50)
    f41=Frame(f4,width=0)
    f41.place(x=100,y=100)
    tbl2=ttk.Treeview(f41,column=('c1','c2','c3'),show='headings',height=5)
    for d,e,f in [('#1',50,'Sno'),('#2',350,'Subjects'),('#3',100,'Marks')]:
            tbl2.column(d,anchor=CENTER,width=e)
            tbl2.heading(d,text=f)            
    tbl2.insert('','end',text='',values=(1,'Multiple intergration ,ODE and complex variables',40))
    tbl2.insert('','end',text='',values=(2,'Python',43))
    tbl2.insert('','end',text='',values=(3,'Eelctrical and electronic engineering',42))
    tbl2.insert('','end',text='',values=(4,'Chemistry',35))
    tbl2.insert('','end',text='',values=(5,'Sustainable design and manufacture',41))
    tbl2.insert('','end',text='',values=(6,'Programing core',38))
    tbl2.pack()

def attendence():
    global f5
    f5=Frame(win3,bg='#f2f1e1',width=720,height=530,highlightthickness=1,highlightbackground='black')
    f5.place(x=250,y=50)
    Exit()
    global cls
    cls=8
    Label(f5,text=' Attendence ',font=('times',15),fg='red',bg='#f2f1e1').place(x=250,y=50)
    c1=Canvas(f5,width=650,height=400,bg='#f2f1e1')
    c1.place(x=50,y=100)
    c1.create_arc(50,50,350,350,fill='red',extent=(fet[13]/(fet[13]+fet[14]))*360,width=1)  
    c1.create_arc(50,50,350,350,fill='cyan',extent=-((fet[14]/(fet[13]+fet[14]))*360),width=1)  
    c1.create_rectangle(450,150,500,190,fill='red',width=1)
    c1.create_rectangle(450,210,500,250,fill='cyan',width=1)
    Label(c1,text='PRESENT',font=('cambria',14),bg='#f2f1e1').place(x=520,y=155)
    Label(c1,text=str(round((fet[13]/(fet[13]+fet[14]))*100,2))+'%',font=('cambria',10),bg='red').place(x=455,y=158)  
    Label(c1,text='ABSENT',font=('cambria',14),bg='#f2f1e1').place(x=520,y=215)  
    Label(c1,text=str(round((fet[14]/(fet[13]+fet[14]))*100,2))+'%',font=('cambria',10),bg='cyan').place(x=455,y=218)


def home():
    global win3
    win3=Tk()#Toplevel(win)
    win3.title('sign up')
    win3.geometry('1000x600')
    win3.resizable(0,0)
    win3.config(bg='#9fe6e8')
    Exit()
    f=Frame(win3,bg='#f2f1e1',width=200,height=530,highlightbackground='black',highlightthickness=1)
    f.place(x=30,y=50)
    '''img=PhotoImage(file='C:\\Users\\KLU\\Pictures\\usericon.png')
    Label(f,image=img).place(x=5,y=5)  #width=180 '''
    c2=Canvas(f,width=160,height=180,highlightbackground='grey',highlightthickness=1)
    c2.place(x=20,y=8)
    c2.create_oval(50,30,110,110)
    c2.create_arc(0,110,160,280,extent=180)
    Label(f,text=fet[2][:16].title(),font=('times',18),fg='blue',bg='#f2f1e1').place(x=10,y=200)
    Button(f,text='Details',font=('arial',10),bd=0,bg='orange',width=18,height=2,command=details).place(x=25,y=250)
    Button(f,text='Fees',font=('arial',10),bd=0,bg='orange',width=18,height=2,command=fees).place(x=25,y=300)
    Button(f,text='Exams',font=('arial',10),bd=0,bg='orange',width=18,height=2,command=exams).place(x=25,y=350)
    Button(f,text='Attendence',font=('arial',10),bd=0,bg='orange',width=18,height=2,command=attendence).place(x=25,y=400)
    global cls
    cls=4
    global f1
    f1=Frame(win3,bg='#f2f1e1',width=720,height=530,highlightthickness=1,highlightbackground='black')
    f1.place(x=250,y=50)
    Label(f1,text='Welcome!',font=('times',30),fg='blue',bg='#f2f1e1').place(x=220,y=180)
    Label(f1,text=fet[2].title().center(40,' '),font=('times',30),fg='blue',bg='#f2f1e1').place(x=25,y=230)
    Button(win3,text=' Sign out ',command=signout,padx=5,pady=5,bd=0).place(x=930,y=2)
    Label(win3,text=str(datetime.now().date()),font=('times',12),fg='blue',bg='#9fe6e8').place(x=30,y=5)
    Label(win3,text=str(datetime.now().time())[:-10],font=('times',12),fg='blue',bg='#9fe6e8').place(x=120,y=5)

cls=0
#home()
Main()

