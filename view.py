import controller
import logger
from tkinter import *
from tkinter import font

def button_click():
    logger.log("Start program")

root = Tk()
root.title("Калькулятор")
root.geometry("590x260+400+400")
root.resizable(width=False, height=False)

def enter1(event):
    controller.e_1()
def enter2(event):
    controller.e_2()
def enter3(event):
    controller.e_3()
def enter4(event):
    controller.e_4()
def enter5(event):
    controller.e_5()
def enter6(event):
    controller.e_6()
def enter7(event):
    controller.e_7()
def enter8(event):
    controller.e_8()
def enter9(event):
    controller.e_9()
def enter10(event):
    controller.e_pi()
def enter11(event):
    controller.e_0()
def enter12(event):
    controller.e_factorial()
def enter13(event):
    e1_action.delete(0, END) # Очистка поля ввода в UI
    controller.list1_clear() # Обнуление списка с формулой
def enter14(event):
    controller.e_div()
def enter15(event):
    controller.e_leftcom()
def enter16(event):  # удаление последнего символа в поле ввода в UI
    e1_action.delete(e1_action.index(END) - 1)
    controller.e_del_last_symbol()
def enter17(event):
    controller.e_plus()
def enter18(event):
    controller.e_rightcom()
def enter19(event):
    controller.e_signchange()
def enter20(event):
    controller.e_minus()
def enter21(event):
    controller.e_dot()
def enter22(event):
    controller.square()
def enter23(event):
    controller.e_mult()
def enter24(event):
    controller.e_exp_2
def enter25(event):
    controller.e_exp()
def enter26(event):
    controller.e_sin()
def enter27(event):
    controller.e_log()
def enter28(event):
    controller.e_cos()
def enter29(event):
    controller.e_ten_exp()
def enter30(event):
    controller.e_tg()
def enter31(event):
    controller.e_mod()
def enter32(event):
    controller.e_equals()
def enter33(event):
    controller.print_log()

l2 = Label(root, text='=', font=("Arial", 14)).place(x = 420, y = 10)

b1 = Button(root, text="1", width=3, height=1, font=("Arial Black", 14))
b2 = Button(root, text="2", width=3, height=1, font=("Arial Black", 14))
b3 = Button(root, text="3", width=3, height=1, font=("Arial Black", 14))
b4 = Button(root, text="4", width=3, height=1, font=("Arial Black", 14))
b5 = Button(root, text="5", width=3, height=1, font=("Arial Black", 14))
b6 = Button(root, text="6", width=3, height=1, font=("Arial Black", 14))
b7 = Button(root, text="7", width=3, height=1, font=("Arial Black", 14))
b8 = Button(root, text="8", width=3, height=1, font=("Arial Black", 14))
b9 = Button(root, text="9", width=3, height=1, font=("Arial Black", 14))
b10 = Button(root, text="π", width=3, height=1, font=("Arial Black", 14))
b11 = Button(root, text="0", width=3, height=1, font=("Arial Black", 14))
b12 = Button(root, text="n!", width=3, height=1, font=("Arial Black", 14))
b13 = Button(root, text="C", width=3, height=1, font=("Arial Black", 14))
b14 = Button(root, text="÷", width=3, height=1, font=("Arial Black", 14))
b15 = Button(root, text="(", width=3, height=1, font=("Arial Black", 14))
b16 = Button(root, text="<=", width=3, height=1, font=("Arial Black", 14))
b17 = Button(root, text="+", width=3, height=1, font=("Arial Black", 14))
b18 = Button(root, text=")", width=3, height=1, font=("Arial Black", 14))
b19 = Button(root, text="±", width=3, height=1, font=("Arial Black", 14))
b20 = Button(root, text="-", width=3, height=1, font=("Arial Black", 14))
b21 = Button(root, text=",", width=3, height=1, font=("Arial Black", 14))
b22 = Button(root, text="√", width=3, height=1, font=("Arial Black", 14))
b23 = Button(root, text="*", width=3, height=1, font=("Arial Black", 14))
b24 = Button(root, text="x^2", width=3, height=1, font=("Arial Black", 14))
b25 = Button(root, text="x^y", width=3, height=1, font=("Arial Black", 14))
b26 = Button(root, text="sin", width=3, height=1, font=("Arial Black", 14))
b27 = Button(root, text="log", width=3, height=1, font=("Arial Black", 14))
b28 = Button(root, text="cos", width=3, height=1, font=("Arial Black", 14))
b29 = Button(root, text="10^x", width=3, height=1, font=("Arial Black", 14))
b30 = Button(root, text="tg", width=3, height=1, font=("Arial Black", 14))
b31 = Button(root, text="mod", width=3, height=1, font=("Arial Black", 14))
b32 = Button(root, text="=", width=3, height=1, font=("Arial Black", 14))
b33 = Button(root, text="Журнал", width=7, height=1, font=("Arial", 14))

v1 = DoubleVar()
v2 = DoubleVar()

e1_action = Entry(root, textvariable = v1, width = 36, justify = LEFT,
        font=font.Font(family="Arial", size=14))
e1_action.place(x=10, y=10)
e1_action.delete(0, END)
e2_result = Entry(root, textvariable = v2, width = 10, justify = LEFT,
        font=font.Font(family="Arial", size=14))
e2_result.place(x = 450, y = 10)
e2_result.delete(0, END)

b1.bind('<Button-1>', enter1)
b1.place(x = 10, y = 40)
b2.bind('<Button-1>', enter2)
b2.place(x = 60, y = 40)
b3.bind('<Button-1>', enter3)
b3.place(x = 110, y = 40)
b4.bind('<Button-1>', enter4)
b4.place(x = 10, y = 90)
b5.bind('<Button-1>', enter5)
b5.place(x = 60, y = 90)
b6.bind('<Button-1>', enter6)
b6.place(x = 110, y = 90)
b7.bind('<Button-1>', enter7)
b7.place(x = 10, y = 140)
b8.bind('<Button-1>', enter8)
b8.place(x = 60, y = 140)
b9.bind('<Button-1>', enter9)
b9.place(x = 110, y = 140)
b10.bind('<Button-1>', enter10)
b10.place(x = 10, y = 190)
b11.bind('<Button-1>', enter11)
b11.place(x = 60, y = 190)
b12.bind('<Button-1>', enter12)
b12.place(x = 110, y = 190)
b13.bind('<Button-1>', enter13)
b13.place(x = 160, y = 40)
b14.bind('<Button-1>', enter14)
b14.place(x = 210, y = 40)
b15.bind('<Button-1>', enter15)
b15.place(x = 260, y = 40)
b16.bind('<Button-1>', enter16)
b16.place(x = 160, y = 90)
b17.bind('<Button-1>', enter17)
b17.place(x = 210, y = 90)
b18.bind('<Button-1>', enter18)
b18.place(x = 260, y = 90)
b19.bind('<Button-1>', enter19)
b19.place(x = 160, y = 140)
b20.bind('<Button-1>', enter20)
b20.place(x = 210, y = 140)
b21.bind('<Button-1>', enter21)
b21.place(x = 260, y = 140)
b22.bind('<Button-1>', enter22)
b22.place(x = 160, y = 190)
b23.bind('<Button-1>', enter23)
b23.place(x = 210, y = 190)
b24.bind('<Button-1>', enter24)
b24.place(x = 260, y = 190)
b25.bind('<Button-1>', enter25)
b25.place(x = 310, y = 40)
b26.bind('<Button-1>', enter26)
b26.place(x = 360, y = 40)
b27.bind('<Button-1>', enter27)
b27.place(x = 310, y = 90)
b28.bind('<Button-1>', enter28)
b28.place(x = 360, y = 90)
b29.bind('<Button-1>', enter29)
b29.place(x = 310, y = 140)
b30.bind('<Button-1>', enter30)
b30.place(x = 360, y = 140)
b31.bind('<Button-1>', enter31)
b31.place(x = 310, y = 190)
b32.bind('<Button-1>', enter32)
b32.place(x = 360, y = 190)
b33.bind('<Button-1>', enter33)
b33.place(x = 450, y = 40)

root.mainloop()
logger.log("Start program")