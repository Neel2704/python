import tkinter as tk
win=tk.Tk()
win.title('CALCULATOR')
win.resizable(False,False)
win.geometry('273x326')

def button_click(num):
    global i
    i+=1
    display.insert(i,num)
def delete():
    display.delete(0, 'end')
def operations(o):
    global i
    global y
    i+=1
    
    if o==11: 
        display.insert(i,'x')
      
    elif o==12:
        display.insert(i,'÷')
        
    elif o==13:
        display.insert(i,'-')

    elif o==14:
        display.insert(i,'+')
 
def equal():
    global l
    global i
    z=0
    y=''
    x=str(display.get()) 
    k=0
    while k<len(x):
        s=x[k]
        if k!=len(x)-1 and x[k]==')' and x[k+1]=='(':
            y+=x[k]+'*'
            k+=1
            continue
        if k!=len(x)-1 and x[k]==')' and x[k+1].isdigit():
            s=')*'
        if k!=0 and x[k-1].isdigit() and x[k]=='(':
            s='*('
        k+=1
        y+=s
    x=y
    print(x)
            
    x=x.replace('÷','/')
    x=x.replace('x','*')
    display.delete(0, 'end')
    try:
        z=eval(x)
    except SyntaxError:
        z=eval(x.lstrip('0'))
        pass
    display.insert(i,z)
def rem():
    x=str(display.get())
    x=x[0:-1]
    display.delete(0,'end')
    display.insert(0,x)
i=-1
display=tk.Entry(win,borderwidth=1,relief='solid',width=18,bg='white',font=('comic sans ms',18,'bold'))
mainwin=tk.Frame(win)
display.pack(anchor='w')
operation=tk.Frame(win,bg='gray40')
mainwin.pack(side='left')
operation.pack(side='left')
win1=tk.Frame(mainwin,borderwidth='3')
win2=tk.Frame(mainwin,borderwidth='3')
win3=tk.Frame(mainwin,borderwidth='3')
win4=tk.Frame(mainwin,borderwidth='3')
win5=tk.Frame(mainwin,borderwidth='3')
g='grey40'
w='white'

#DEFINING BUTTONS
brac1=tk.Button(win5,text='(',font=('comic sans ms',15,'bold'),padx=20,pady=2.4,relief='flat',command=lambda:button_click('('))
brac2=tk.Button(win5,text=')',font=('comic sans ms',15,'bold'),padx=20,relief='flat',borderwidth='3',command=lambda:button_click(')'))
rem=tk.Button(win5,text='del',font=('comic sans ms',15,'bold'),padx=18,relief='flat',borderwidth='3',command=rem)
one=tk.Button(win1,text='1',font=('comic sans ms',15,'bold'),padx=20,relief='flat',command=lambda:button_click(1))
two=tk.Button(win1,text='2',font=('comic sans ms',15,'bold'),padx=20,relief='flat',command=lambda:button_click(2))
three=tk.Button(win1,text='3',font=('comic sans ms',15,'bold'),padx=20,relief='flat',command=lambda:button_click(3))
four=tk.Button(win2,text='4',font=('comic sans ms',15,'bold'),padx=20,relief='flat',command=lambda:button_click(4))
five=tk.Button(win2,text='5',font=('comic sans ms',15,'bold'),padx=20,relief='flat',command=lambda:button_click(5))
six=tk.Button(win2,text='6',font=('comic sans ms',15,'bold'),padx=20,relief='flat',command=lambda:button_click(6))
seven=tk.Button(win3,text='7',font=('comic sans ms',15,'bold'),padx=20,relief='flat',command=lambda:button_click(7))
eight=tk.Button(win3,text='8',font=('comic sans ms',15,'bold'),padx=20,relief='flat',command=lambda:button_click(8))
nine=tk.Button(win3,text='9',font=('comic sans ms',15,'bold'),padx=20,relief='flat',command=lambda:button_click(9))
zero=tk.Button(win4,text='0',font=('comic sans ms',15,'bold'),padx=20,relief='flat',command=lambda:button_click(0))
clear=tk.Button(win4,text='C',font=('comic sans ms',15,'bold'),padx=17,relief='flat',command=delete)
point=tk.Button(win4,text='.',font=('comic sans ms',15,'bold'),padx=20,relief='flat',command=lambda:button_click('.'))
add=tk.Button(operation,text='+',font=('comic sans ms',17,'bold'),padx=15,pady=1.5,bg=g,fg=w,activebackground=g,activeforeground=w,relief='flat',command=lambda:operations(14))
equal=tk.Button(operation,text='=',font=('comic sans ms',17,'bold'),padx=16,pady=1.5,bg='orange',fg='white',activeforeground='white',activebackground='orange',relief='flat',command=equal)
minus=tk.Button(operation,text='-',font=('comic sans ms',17,'bold'),padx=15,pady=1.5,bg=g,fg=w,activebackground=g,activeforeground=w,relief='flat',command=lambda:operations(13))
divide=tk.Button(operation,text='÷',font=('comic sans ms',17,'bold'),padx=15,pady=1.5,bg=g,fg=w,activebackground=g,activeforeground=w,relief='flat',command=lambda:operations(12))
multiply=tk.Button(operation,text='x',font=('comic sans ms',17,'bold'),padx=15,pady=0.5,bg=g,fg=w,activebackground=g,activeforeground=w,relief='flat',command=lambda:operations(11))

#DISPLAYING BUTTONS
brac1.pack(side='left')
brac2.pack(side='left')
rem.pack(side='left')
win5.pack()

one.pack(side='left')
two.pack(side='left')
three.pack(side='left')
win1.pack()

four.pack(side='left')
five.pack(side='left')
six.pack(side='left')
win2.pack()
minus

seven.pack(side='left')
eight.pack(side='left')
nine.pack(side='left')
win3.pack()


point.pack(side='left')
zero.pack(side='left')
clear.pack(side='left')
win4.pack()

multiply.pack()
divide.pack()
minus.pack()
add.pack()
equal.pack()


win.mainloop()
