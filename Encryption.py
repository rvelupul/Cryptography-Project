from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfile
 
def raise_frame(f):
    f.tkraise()
 
def finish():
    r.destroy()
def fr1():
    Clear()
    raise_frame(Fr1)
def fr2():
    Clear()
    raise_frame(Fr2) 
def fr3():
    Clear()
    raise_frame(Fr3)
def fr4():
    Clear()
    raise_frame(Fr4)
def fr5():
    Clear()
    raise_frame(Fr5)
def fr6():
    Clear()
    raise_frame(Fr6) 
def fr7():
    Clear()
    raise_frame(Fr7)
def fr8():
    Clear()
    raise_frame(Fr8)

#----------------------------Encryption code-------------------------------------------------------
ts=0
def fun1():
    global asky9
    global ts
    global skey
    txt=str(e1.get()) 
    key=str(e2.get())
    
    ts=1
    #txt=txt.upper()
    if(len(txt)!=0 and len(key)!=0):
        n=len(txt)
        key=key.replace(' ','')
        if(key.isnumeric()):
            if(int(key)>=1 or int(key)<=26):
                skey=key
                asky=''
                asky9=''
                for i in range(n):
                    a9=ord(txt[i])+int(key)
                    a9=a9-64
                    #a9=a9%26
                    ce=chr(a9+64)
                    
                    asky+=str(ce)+' '
                    asky9+=str(ord(ce))+' '
                x1.set(asky)
                e1.configure(state='disabled')
                e2.configure(state='disabled')
        else:
            messagebox.showinfo('Message Box','Shift key should be number')
    else:
        messagebox.showinfo('Message Box','Enter Plain text and Shift key')

def fun2():
    global asky9
    global ts
    if(ts==1):
        ts=2
        x2.set(asky9)
    else:
        messagebox.showinfo('Message Box','Please click the previous button')

def fun3():
    global asky9
    global ao
    global ct
    global k9
    global ts
    global ks
    if(ts==2):
        ts=3
        ks=1
        asky9=asky9.split(' ')
        asky9=asky9[:-1]
        k9=''
        ao=''
        ct=''
        for i in range(len(asky9)):
            k8=oct(int(asky9[i]))
            k7=int(asky9[i])
            k87=(int(k8[2:])+k7)%256
            k9+=str(k8[2:])+' '
            ao+=str(k87)+' '
            ct+=str(chr(k87))
        x3.set(k9)
    else:
        messagebox.showinfo('Message Box','Please click the previous button')

def fun4():
    global ao
    global ts
    if(ts==3):
        ts=4
        x4.set(ao)
    else:
        messagebox.showinfo('Message Box','Please click the previous button')


def fun5():
    global ct
    global ts
    if(ts==4):
        ts=5
        x5.set(ct)
    else:
        messagebox.showinfo('Message Box','Please click the previous button')
    
def SaveKey():
    global k9
    global skey
    global ks
    if(ks==1):
        f = asksaveasfile(mode='w', defaultextension=".txt")
        if f is None:
            return
        f.write(str(skey+' '+k9))
        f.close()
        messagebox.showinfo('Message Box','Key is saved successfully')
    else:
        messagebox.showinfo('Message Box','Please click the octal button')
def SaveCode():
    global ct
    global ts
    if(ts==5):
        
        f = asksaveasfile(mode='w', defaultextension=".txt")
        if f is None:
            return
        f.write(str(ct))
        f.close()
        messagebox.showinfo('Message Box','Cipher text is saved successfully')
    else:
        messagebox.showinfo('Message Box','Please click the previous button')


#----------------------------Decryption code-------------------------------------------------------
tq=0
tqk=0
def OpenCode():
    global D
    global tq
    D=''
    file=askopenfile(mode='r',filetypes=[('All files','*.txt')])
    if file is not None:
        D=file.read()
        tq=1
    x6.set(D)
def fun6():
    global D
    global tq
    if(tq==1):
        tq=2
        as1=''
        for i in range(len(D)):
            as1+=str(ord(D[i]))+' '
        x7.set(as1)
    else:
        messagebox.showinfo('Message Box','Please click the previous button')
def OpenKey():
    global Okey
    global tqk
    Okey=''
    file=askopenfile(mode='r',filetypes=[('All files','*.txt')])
    if file is not None:
        Okey=file.read()
        tqk=1
    x8.set(Okey[1:])
def fun7():
    global Okey
    global D
    global shiftk
    global oc
    global pt
    global tq
    global tqk
    as1=''
    for i in range(len(D)):
        as1+=str(ord(D[i]))+' '
    as1=as1.split(' ')
    as1=as1[:-1]
    
    shiftk=Okey[0]
    od=Okey[2:-1]
    od=od.split(' ')
    
    oc=''
    ao2=''
    pt=''
    for i in range(len(od)):
        h2=(int(as1[i])-int(od[i]))%256
        h3=h2-int(shiftk)
        ao2+=str(h2)+' '
        oc+=str(h3)+' '
        pt+=str(chr(h3))
    x9.set(ao2)
        
def fun8():
    global tq
    if(tq==2):
        tq=4
        global shiftk
        x10.set(shiftk)
    else:
        messagebox.showinfo('Message Box','Please click the previous button')

def fun9():
    global oc
    global tq
    if(tq==4):
        tq=5
        x11.set(oc)
    else:
        messagebox.showinfo('Message Box','Please click the previous button')

def fun10():
    global pt
    global tq
    if(tq==5):
        tq=0
        x12.set(pt)
    else:
        messagebox.showinfo('Message Box','Please click the previous button')

r = Tk()
Fr0 = Frame(r)
Fr1 = Frame(r)
Fr2 = Frame(r)
Fr3 = Frame(r)
Fr4 = Frame(r)
Fr5 = Frame(r)
Fr6 = Frame(r)
Fr7 = Frame(r)
Fr8 = Frame(r)


Fr0.place(x = 0,y = 0,height=400, width=1100)
Fr1.place(x = 0,y = 157,height=600, width=1100)
Fr2.place(x = 0,y = 157,height=600, width=1100)
Fr3.place(x = 0,y = 157,height=600, width=1100)
Fr4.place(x = 0,y = 157,height=600, width=1100)
Fr5.place(x = 0,y = 157,height=600, width=1100)
Fr6.place(x = 0,y = 157,height=600, width=1100)
Fr7.place(x = 0,y = 157,height=600, width=1100)
Fr8.place(x = 0,y = 157,height=600, width=1100)


Fr0.config(bg='white')

def Clear():
    ts=0
    tq=0
    tqk=0
    e1.configure(state='normal')
    e2.configure(state='normal')
    e1.delete(0,END)
    e2.delete(0,END)
    x1.set('')
    x2.set('')
    x3.set('')
    x4.set('')
    x5.set('')
    x6.set('')
    x7.set('')
    x8.set('')
    x9.set('')
    x10.set('')
    x11.set('')
    x12.set('')
   

x1=StringVar()
x2=StringVar()
x3=StringVar()
x4=StringVar()
x5=StringVar()
x6=StringVar()
x7=StringVar()
x8=StringVar()
x9=StringVar()
x10=StringVar()
x11=StringVar()
x12=StringVar()

#HeadingPage

ph=ImageTk.PhotoImage(Image.open("logo.jpg"))
lab1 = Label(Fr0,bg="black", text = "",image=ph, width=1200,height=0).place(x = 0, y = -2)


#------------------StartPage Fr1---------------------------------------------------------------------------
ph100=ImageTk.PhotoImage(Image.open("1.jpg"))
lab1 = Label(Fr1,image=ph100, width=1100).place(x = 0, y = 0)

lab2 = Label(Fr1, justify="left",text = """A Modified Symmetric Key Cryptography
    Method for Secure Data Transmission""",
                 fg="black",bg="white", font = "rockwell 30 bold",height=3).place(x = 145,y=100)




lab5 = Label(Fr1, text = """
PRESENTED BY

Rushil Velupula

""",
                 bg = "white",
                 fg = "#000080",
		 font = "Helvetica 12 bold",height=4,width=23).place(x = 400,y=300)


but1 = Button(Fr1, text = "Proceed",
            fg="black",bg="#AFEEEE",bd=5, font = "rockwell 14 bold",height=1,width=8, command = fr4).place(x = 110, y = 300)
but2 = Button(Fr1, text = "Close",
            fg="black",bg="#AFEEEE",bd=5,font = "Elephant 14 bold",height=1,width=8,command=finish).place(x = 870, y =300)


#-------------------------Abstract----Fr-2--------------------

#AFEEEE
#----------------------CURRENT PROPOSED SYSTEM------frame-3 --------------------

ph3=Image
#----------------Menu Page Fr-4 -------------------------------------------------------------------------

ph4=ImageTk.PhotoImage(Image.open("1.jpg"))
lab1 = Label(Fr4,image=ph4, width=1100).place(x = 0, y = 0)

lab2 = Label(Fr4, justify="left",text = "A Modified Symmetric Key Cryptography Method for Secure Data Transmission",
                 fg="black",bg="white", font = "Latin 14 bold",height=2).place(x = 190,y=25)

ph10=ImageTk.PhotoImage(Image.open("3.jpg"))
lab1 = Label(Fr4,image=ph10).place(x = 50, y = 80)


but4 = Button(Fr4, text = "Encryption",
            fg="black",bg="#AFEEEE",bd=5, font = "Helvetica 12 bold",height=1,width=10,command = fr5).place(x = 280, y = 420)
but5 = Button(Fr4, text = "Decryption",
            fg="black",bg="#AFEEEE",bd=5, font = "Helvetica 12 bold",height=1,width=10,command = fr6).place(x = 720, y = 420)

but2 = Button(Fr4, text = "Home",
            fg="black",bg="#AFEEEE",bd=5, font = "Helvetica 12 bold",height=2,width=10,command = fr1).place(x = 50, y = 5)
but7 = Button(Fr4, text = "Close",
            fg="black",bg="#AFEEEE",bd=5, font = "Helvetica 12 bold",height=2,width=10,command = finish).place(x = 950, y = 5)



#--------------------Encryption 1  ----Fr-5---------------------------------------------------------------------------------

ph5=ImageTk.PhotoImage(Image.open("1.jpg"))
lab1 = Label(Fr5,image=ph5, width=1100).place(x = 0, y = 0)

lab2 = Label(Fr5, justify="left",text = "A Modified Symmetric Key Cryptography Method for Secure Data Transmission",
                 fg="black",bg="white", font = "Latin 14 bold",height=2).place(x = 190,y=25)

l1 = Label(Fr5, text = "Encryption",fg="white",bg="red", font = "Latin 10 bold",height=1).place(x = 5, y =80)

l1 = Label(Fr5, text = "Enter Plain Text",fg="black",bg="white", font = "Latin 12 bold",height=2,width=16).place(x=100, y =80)
e1= Entry(Fr5, fg="black", bg='white',bd=2,font = "Latin 23 bold",width=35)
e1.place(x = 300,y=84)

l4 = Label(Fr5, text = "Enter Shift Key",fg="black",bg="white",bd=5, font = "Helvetica 12 bold",height=2,width=16).place(x=100,y=145)
e2= Entry(Fr5, fg="black",bd=2, bg='white',font = "Latin 23 bold",width=35)
e2.place(x =300,y=146)

b1 = Button(Fr5, text = "Apply Ceasar Cipher",fg="black",bg="#AFEEEE",bd=5, font = "Helvetica 12 bold",height=2,width=16,command = fun1).place(x=100, y =210)
l3= Label(Fr5, textvariable=x1,fg="black",bg="white", font = "Latin 16 bold",width=45,height=2).place(x = 300,y=210)


b2 = Button(Fr5, text = "Convert to ASCII",fg="black",bg="#AFEEEE",bd=5, font = "Helvetica 12 bold",height=2,width=16,command = fun2).place(x=100, y =275)
l3= Label(Fr5, textvariable=x2,fg="black",bg="white", font = "Latin 16 bold",width=45,height=2).place(x = 300,y=275)

b2 = Button(Fr5, text = "Covert to Octal(K)",fg="black",bg="#AFEEEE",bd=5, font = "Helvetica 12 bold",height=2,width=16,command = fun3).place(x=100, y =345)
l3= Label(Fr5,textvariable=x3,fg="black",bg="white", font = "Latin 16 bold",width=45,height=2).place(x = 300,y=345)

b5 = Button(Fr5, text = "Apply (A+O) Mod 256",fg="black",bg="#AFEEEE",bd=5, font = "Helvetica 12 bold",height=2,width=16,command = fun4).place(x=100,y=410)
l3= Label(Fr5, textvariable=x4,fg="black",bg="white", font = "Latin 16 bold",width=45,height=2).place(x = 300,y=410)

b5 = Button(Fr5, text = "Cipher Text",fg="black",bg="#AFEEEE",bd=5, font = "Helvetica 12 bold",height=2,width=16,command = fun5).place(x=100,y=475)
l3= Label(Fr5, textvariable=x5,fg="black",bg="white", font = "Latin 16 bold",width=45,height=2).place(x = 300,y=475)

b8 = Button(Fr5, text = "SaveKey",fg="black",bg="#AFEEEE",bd=5, font = "Helvetica 12 bold",height=2,width=10,command = SaveKey).place(x = 950, y = 345)
b7 = Button(Fr5, text = "SaveCipher",fg="black",bg="#AFEEEE",bd=5, font = "Helvetica 12 bold",height=2,width=10,command=SaveCode).place(x = 950, y = 410)

b8 = Button(Fr5, text = "Clear",fg="black",bg="#AFEEEE",bd=5, font = "Helvetica 12 bold",height=2,width=10,command = Clear).place(x = 950, y = 210)
b8 = Button(Fr5, text = "Prev",fg="black",bg="#AFEEEE",bd=5, font = "Helvetica 12 bold",height=2,width=10,command = fr4).place(x = 950, y = 275)
b7 = Button(Fr5, text = "Next",fg="black",bg="#AFEEEE",bd=5, font = "Helvetica 12 bold",height=2,width=10,command=fr6).place(x = 950, y = 475)

but2 = Button(Fr5, text = "Home",
            fg="black",bg="#AFEEEE",bd=5, font = "Helvetica 12 bold",height=2,width=10,command = fr1).place(x = 50, y = 5)
but7 = Button(Fr5, text = "Close",
            fg="black",bg="#AFEEEE",bd=5, font = "Helvetica 12 bold",height=2,width=10,command = finish).place(x = 950, y = 5)

#--------------------Decryption -------Fr-6---------------------------------------------------------------------------------

ph15=ImageTk.PhotoImage(Image.open("1.jpg"))
lab1 = Label(Fr6,image=ph15, width=1100).place(x = 0, y = 0)

l1 = Label(Fr6, text = "Decryption",fg="white",bg="red", font = "Latin 10 bold",height=1).place(x = 5, y =80)

lab2 = Label(Fr6, justify="left",text = "A Modified Symmetric Key Cryptography Method for Secure Data Transmission",
                 fg="black",bg="white", font = "Latin 14 bold",height=2).place(x = 190,y=25)

b1 = Button(Fr6, text = "Browse CipherText",fg="black",bg="#AFEEEE",bd=5, font = "Helvetica 12 bold",height=2,width=16,command = OpenCode).place(x = 100, y =80)
l3= Label(Fr6, textvariable=x6,fg="black",bg="white", font = "Latin 16 bold",width=45,height=2).place(x = 300,y=80)

b1 = Button(Fr6, text = "Convert to ASCII",fg="black",bg="#AFEEEE",bd=5, font = "Helvetica 12 bold",height=2,width=16,command = fun6).place(x = 100, y =145)
l3= Label(Fr6, textvariable=x7,fg="black",bg="white", font = "Latin 16 bold",width=45,height=2).place(x = 300,y=145)

b1 = Button(Fr6, text = "Browse Octal Key",fg="black",bg="#AFEEEE",bd=5, font = "Helvetica 12 bold",height=2,width=16,command = OpenKey).place(x = 100, y =210)
l3= Label(Fr6, textvariable=x8,fg="black",bg="white", font = "Latin 16 bold",width=45,height=2).place(x = 300,y=210)

b2 = Button(Fr6, text = "Apply (A-O) Mod 256",fg="black",bg="#AFEEEE",bd=5, font = "Helvetica 12 bold",height=2,width=16,command = fun7).place(x =100, y =275)
l3= Label(Fr6, textvariable=x9,fg="black",bg="white", font = "Latin 16 bold",width=45,height=2).place(x = 300,y=275)

b2 = Button(Fr6, text = "Shift Key",fg="black",bg="#AFEEEE",bd=5, font = "Helvetica 12 bold",height=2,width=16,command = fun8).place(x =100, y =345)
l3= Label(Fr6,textvariable=x10,fg="black",bg="white", font = "Latin 16 bold",width=45,height=2).place(x = 300,y=345)

b5 = Button(Fr6, text = "Apply Ceasar Cipher",fg="black",bg="#AFEEEE",bd=5, font = "Helvetica 12 bold",height=2,width=16,command = fun9).place(x =100,y=410)
l3= Label(Fr6, textvariable=x11,fg="black",bg="white", font = "Latin 16 bold",width=45,height=2).place(x = 300,y=410)

b5 = Button(Fr6, text = "Plain Text",fg="black",bg="#AFEEEE",bd=5, font = "Helvetica 12 bold",height=2,width=16,command = fun10).place(x =100,y=475)
l3= Label(Fr6, textvariable=x12,fg="black",bg="white", font = "Latin 16 bold",width=45,height=2).place(x = 300,y=475)

b8 = Button(Fr6, text = "Clear",fg="black",bg="#AFEEEE",bd=5, font = "Helvetica 12 bold",height=2,width=10,command = Clear).place(x = 950, y = 345)
b8 = Button(Fr6, text = "Prev",fg="black",bg="#AFEEEE",bd=5, font = "Helvetica 12 bold",height=2,width=10,command = fr4).place(x = 950, y = 410)
b7 = Button(Fr6, text = "Next",fg="black",bg="#AFEEEE",bd=5, font = "Helvetica 12 bold",height=2,width=10,command=fr7).place(x = 950, y = 475)

but2 = Button(Fr6, text = "Home",
            fg="black",bg="#AFEEEE",bd=5, font = "Helvetica 12 bold",height=2,width=10,command = fr1).place(x = 50, y = 5)
but7 = Button(Fr6, text = "Close",
            fg="black",bg="#AFEEEE",bd=5, font = "Helvetica 12 bold",height=2,width=10,command = finish).place(x = 950, y = 5)

#------------------------Conclusion-----Fr-7--------------------

ph7=ImageTk.PhotoImage(Image.open("1.jpg"))
lab1 = Label(Fr7,image=ph7, width=1100).place(x = 0, y = 0)

lab2 = Label(Fr7, justify="left",text = "A Modified Symmetric Key Cryptography Method for Secure Data Transmission",
                 fg="black",bg="white", font = "Latin 14 bold",height=2).place(x = 190,y=25)

l5= Label(Fr7,text="""__Conclusion__

Information Security has become a very critical part of modern computing systems.  Day by day internet

users are growing rapidly.  So that, it is necessary to secure the data over public transmission medium.

To provide security to data different encryption methods can be used.  The proposed method is a refinement

of existing Caesar cipher method overcoming the drawbacks of the method.  The concept of key is introduced

with Caesar cipher to generalize the encryption concept.  The ciphertext generated by the proposed method

is very hard to understand because of it contains lot of symbols.  This is further extended to complicate

the age old basic method to a cumbersome method inorder to complicate ciphertext.

""", justify="left",fg="black",bg="white",  font = "Helvetica 12 bold",width=90).place(x = 120, y =110)


b9 = Button(Fr7, text = "Prev",fg="black",bg="#AFEEEE",bd=5, font = "Helvetica 14 bold",height=1,width=10,command=fr4).place(x = 400, y = 450)
b10 = Button(Fr7, text = "Next",fg="black",bg="#AFEEEE",bd=5, font = "Helvetica 14 bold",height=1,width=10,command = fr1).place(x = 550, y = 450)

but2 = Button(Fr7, text = "Home",
            fg="black",bg="#AFEEEE",bd=5, font = "Helvetica 12 bold",height=2,width=10,command = fr1).place(x = 50, y = 5)
but7 = Button(Fr7, text = "Close",
            fg="black",bg="#AFEEEE",bd=5, font = "Helvetica 12 bold",height=2,width=10,command = finish).place(x = 950, y = 5)

#-----------------------Thank U------Fr-8--------------------


#------------------------------------------------------------------------

raise_frame(Fr1)
r.geometry("1100x700+100+0")
r.title("A Modified Symmetric Key Cryptography Method for Secure Data Transmission")
r.mainloop()


