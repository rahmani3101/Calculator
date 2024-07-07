from  tkinter import *

calc = Tk()

calc.title('Calculator')
calc.geometry('335x520')

calc.config(bg='black')

expression=""

def show(key):
    global expression
    expression=expression + str(key)
    text_box.config(text=expression)

def clear():
    global expression
    expression=""
    text_box.config(text=expression)

def evaluate():
    global expression
    result=""
    if expression !="":
        try:
            result=eval(expression)
        except:
            result='error'  
    text_box.config(text=result)                   

text_box=Label(calc,text='',width='15',height='2', font=("Ariel",28),bg='white')
text_box.place(x=0,y=0)

btn_c=Button(calc ,command=lambda:clear(), text='C',width=3,height=1 , font=("Ariel",30), bg='#35fec7')
btn_c.place(x=0,y=95)
btn_per=Button(calc ,command=lambda:show('%'), text='%',width=3,height=1 , font=("Ariel",30), bg='#ADD8E6')
btn_per.place(x=85,y=95)
btn_div=Button(calc ,command=lambda:show('/'), text='/',width=3,height=1 , font=("Ariel",30), bg='#ADD8E6')
btn_div.place(x=170,y=95)
btn_mul=Button(calc ,command=lambda:show('*'), text='*',width=3,height=1 , font=("Ariel",30), bg='#ADD8E6')
btn_mul.place(x=255,y=95)


btn_7=Button(calc ,command=lambda:show('7'), text='7',width=3,height=1 , font=("Ariel",30), bg='grey')
btn_7.place(x=0,y=180)
btn_8=Button(calc ,command=lambda:show('8'), text='8',width=3,height=1 , font=("Ariel",30), bg='grey')
btn_8.place(x=85,y=180)
btn_9=Button(calc ,command=lambda:show('9'), text='9',width=3,height=1 , font=("Ariel",30), bg='grey')
btn_9.place(x=170,y=180)
btn_sub=Button(calc ,command=lambda:show('-'), text='-',width=3,height=1 , font=("Ariel",30), bg='#ADD8E6')
btn_sub.place(x=255,y=180)

#third row
btn_4=Button(calc ,command=lambda:show('4'), text='4',width=3,height=1 , font=("Ariel",30), bg='grey')
btn_4.place(x=0,y=265)
btn_5=Button(calc ,command=lambda:show('5'), text='5',width=3,height=1 , font=("Ariel",30), bg='grey')
btn_5.place(x=85,y=265)
btn_6=Button(calc ,command=lambda:show('6'), text='6',width=3,height=1 , font=("Ariel",30), bg='grey')
btn_6.place(x=170,y=265)
btn_add=Button(calc , command=lambda:show('+'),text='+',width=3,height=1 , font=("Ariel",30), bg='#ADD8E6')
btn_add.place(x=255,y=265)


#fourth row
btn_1=Button(calc ,command=lambda:show('1'), text='1',width=3,height=1 , font=("Ariel",30), bg='grey')
btn_1.place(x=0,y=350)
btn_2=Button(calc , command=lambda:show('2'),text='2',width=3,height=1 , font=("Ariel",30), bg='grey')
btn_2.place(x=85,y=350)
btn_3=Button(calc ,command=lambda:show('3'), text='3',width=3,height=1 , font=("Ariel",30), bg='grey')
btn_3.place(x=170,y=350)
btn_eq=Button(calc ,command=lambda: evaluate(), text='=',width=3,height=3 , font=("Ariel",30), bg='#00c04b')
btn_eq.place(x=255,y=350)

#last
btn_0=Button(calc , command=lambda:show('0'),text='0',width=3,height=1 , font=("Ariel",30), bg='grey')
btn_0.place(x=0,y=435)
btn_close=Button(calc ,command=lambda:show('('), text='(',width=3,height=1 , font=("Ariel",30), bg='#ADD8E6')
btn_close.place(x=85,y=435)
btn_open=Button(calc ,command=lambda:show(')'), text=')',width=3,height=1 , font=("Ariel",30), bg='#ADD8E6')
btn_open.place(x=170,y=435)



calc.mainloop()