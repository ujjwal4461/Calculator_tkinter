from tkinter import *


clist = []


def num_press(key):
    inp.config(state="normal")
    entered_val = inp.get()
    cmbd_txt = entered_val + key
    inp.delete(0,'end')
    inp.insert(0,cmbd_txt)
    inp.config(state="readonly")


def opp_press(key):
    inp.config(state="normal")
    evalue1 = inp.get()
    try:
        enum1 = float(evalue1)
        clist.append(enum1)
    except ValueError:
        print('Not a valid entry')
    clist.append(key)
    inp.delete(0,'end')
    inp.config(state="readonly")
    

def eq_press():
    inp.config(state="normal")
    evalue2 = inp.get()
    clen = len(clist)
    if(clen!=2):
        print("not a valid expression")    
    else:
        try:
            enum2 = float(evalue2)
            clist.append(enum2)
        except ValueError:
            print("not a valid no")
        if(clist[1] == '+'):
            result = clist[0] + enum2
        elif(clist[1] == '-'):
            result = clist[0] - enum2
        elif(clist[1] == '*'):
            result = clist[0] * enum2
        elif(clist[1] == '/'):
            result = clist[0] / enum2
        else:
            print("no a valid opetaration")
        inp.delete(0,'end')
        clist.clear()
        inp.insert(0,result)
    inp.config(state="readonly")


def ac_press():
    inp.config(state="normal")
    inp.delete(0,'end')
    clist.clear()
    inp.config(state="readonly")


def neg_press():
    inp.config(state="normal")
    num = inp.get()
    num = '-' + num
    inp.delete(0,'end')
    inp.insert(0,num)
    inp.config(state="readonly")


def clr_press():
    inp.config(state="normal")
    get_str = inp.get()
    if(len(get_str) != 1):
        get_num = int(get_str)
        new_num = get_num//10
        new_str = str(new_num)
        inp.delete(0,'end')
        inp.insert(0,new_str)
    else:
        inp.delete(0,'end')
    inp.config(state="readonly")


root = Tk()
root.title("CaLcUlAtOr")
root.geometry("390x520")
root.resizable(width=FALSE,height=FALSE)
root.config(background='grey')


txt_styl = ('Times Roman New',44,'italic')
btn_styl = ('Times Roman New',50,'bold')


inp = Entry(root,font=('Times Roman New',34,'italic'),justify=RIGHT)
inp.place(x=10, y=10, width=370, height=50)
inp.config(state="readonly")
btn1 = Button(root,text="7", font=btn_styl, command=lambda: num_press('7'))
btn1.place(x=10, y=70, width=85, height=80)
btn2 = Button(root,text="8", font=btn_styl, command=lambda: num_press('8'))
btn2.place(x=105, y=70, width=85, height=80)
btn3 = Button(root,text="9", font=btn_styl, command=lambda: num_press('9'))
btn3.place(x=200, y=70, width=85, height=80)
btn4 = Button(root,text="4", font=btn_styl, command=lambda: num_press('4'))
btn4.place(x=10, y=160, width=85, height=80)
btn5 = Button(root,text="5", font=btn_styl, command=lambda: num_press('5'))
btn5.place(x=105, y=160, width=85, height=80)
btn6 = Button(root,text="6", font=btn_styl, command=lambda: num_press('6'))
btn6.place(x=200, y=160, width=85, height=80)
btn7 = Button(root,text="1", font=btn_styl, command=lambda: num_press('1'))
btn7.place(x=10, y=250, width=85, height=80)
btn8 = Button(root,text="2", font=btn_styl, command=lambda: num_press('2'))
btn8.place(x=105, y=250, width=85, height=80)
btn9 = Button(root,text="3", font=btn_styl, command=lambda: num_press('3'))
btn9.place(x=200, y=250, width=85, height=80)
btn0 = Button(root,text="0", font=btn_styl, command=lambda: num_press('0'))
btn0.place(x=105, y=340, width=85, height=80)

btneq = Button(root,text="=", font=btn_styl, command=lambda: eq_press())
btneq.place(x=295, y=430, width=85, height=80)

btnp = Button(root,text="+", font=btn_styl, command=lambda: opp_press('+'))
btnp.place(x=295, y=70, width=85, height=80)
btns = Button(root,text="-", font=btn_styl, command=lambda: opp_press('-'))
btns.place(x=295, y=160, width=85, height=80)
btnm = Button(root,text="*", font=btn_styl, command=lambda: opp_press('*'))
btnm.place(x=295, y=250, width=85, height=80)
btnd = Button(root,text="/", font=btn_styl, command=lambda: opp_press('/'))
btnd.place(x=295, y=340, width=85, height=80)

btnac = Button(root,text="AC", font=btn_styl, command=lambda: ac_press())
btnac.place(x=10, y=430, width=180, height=80)
btncl = Button(root,text="c", font=btn_styl, command=lambda: clr_press())
btncl.place(x=200, y=430, width=85, height=80)

btndt = Button(root,text=".", font=btn_styl, command=lambda: num_press('.'))
btndt.place(x=10, y=340, width=85, height=80)
btnms = Button(root,text="-", font=btn_styl, command=lambda: neg_press())
btnms.place(x=200, y=340, width=85, height=80)


root.mainloop()
