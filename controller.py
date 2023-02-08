from tkinter import *
import view
import logger
import functions

a1 = str("")
_list1 = ["o"]

def list1_clear(): # очищает list1 и a1 при нажатии C
    global _list1, a1
    _list1 = ["o"]
    a1 = str("") # a1 - добавляемая в число цифра

def add_element(): # удаляет значение list1 с предыдущим индексом при наборе цифр (для формирования числа из набираемых цифр)
    global _list1, c
    _list1.append(float(a1))
    c = _list1[len(_list1) - 2]
    if c != "10^" and c != "+" and c != "-" and c != "*" and c != "/" and c != "(" and c != "^" and c != "sin" and c != "log" and c != "cos" and c != "tg" and c != "!" and c != "√" and c != "^":
        del _list1[len(_list1) - 2]

def left_cursor():
    position = view.e1_action.index(INSERT) #
    view.e1_action.icursor(position - 1) # смещение курсора влево в поле Entry на одну позицию 

def e_equals(): # нажатие "=" и вызов функции решения 
    logger.log("выражение:{}".format((' '.join(map(str, _list1)))))
    view.e2_result.delete(0, END) # очисткой поля вывода ререзультата
    functions.brackets(_list1)

def e_1():
    global a1
    a1 = a1 + "1"
    view.e1_action.insert(INSERT, "1")
    add_element()
def e_2():
    global a1
    a1 = a1 + "2"
    view.e1_action.insert(INSERT, "2")
    add_element()
def e_3():
    global a1
    a1 = a1 + "3"
    view.e1_action.insert(INSERT, "3")
    add_element()
def e_4():
    global a1
    a1 = a1 + "4"
    view.e1_action.insert(INSERT, "4")
    add_element()
def e_5():
    global a1
    a1 = a1 + "5"
    view.e1_action.insert(INSERT, "5")
    add_element()
def e_6():
    global a1
    a1 = a1 + "6"
    view.e1_action.insert(INSERT, "6")
    add_element()
def e_7():
    global a1
    a1 = a1 + "7"
    view.e1_action.insert(INSERT, "7")
    add_element()
def e_8():
    global a1
    a1 = a1 + "8"
    view.e1_action.insert(INSERT, "8")
    add_element()
def e_9():
    global a1
    a1 = a1 + "9"
    view.e1_action.insert(INSERT, "9")
    add_element()
def e_0():
    global a1
    a1 = a1 + "0"
    view.e1_action.insert(INSERT, "0")
    add_element()
def e_dot():
    global a1
    a1 = a1 + "."
    view.e1_action.insert(INSERT, ".")
    add_element()
def e_div():
    global a1
    view.e1_action.insert(INSERT, "/")
    _list1.append("/")
    a1 = str("")  # очищаем a1

def e_del_last_symbol():
    global _list1
    s = _list1[len(_list1) - 1] #  получаем правый элемент списка _list1
    del _list1[len(_list1) - 1] #  удаляем правый элемент списка _list1
    p = list(str(s))  # правый элемент списка _list1 превратили в список р
    del p[len(p) - 1] # удаляем правый элемент списка р 
    s = "".join(map(str, p)) # делаем из списка -> str
    _list1.append(s) #  возвращаем ранее удаленный и отредактированный правый элемент списка _list1

def e_leftcom():
    global a1
    view.e1_action.insert(INSERT, "(")
    _list1.append("(")
    a1 = str("")  # очищаем a1

def e_plus():
    global a1
    view.e1_action.insert(INSERT, "+")
    _list1.append("+")
    a1 = str("")  # очищаем a1

def e_rightcom():
    global a1
    view.e1_action.insert(INSERT, ")")
    _list1.append(")")
    a1 = str("")  # очищаем a1

def e_minus():
    global a1
    view.e1_action.insert(INSERT, "-")
    _list1.append("-")
    a1 = str("")  # очищаем a1

def e_mult():
    global a1
    view.e1_action.insert(INSERT, "*")
    _list1.append("*")
    a1 = str("")  # очищаем a1

def e_signchange():
    global a1
    view.e1_action.insert(INSERT, "-")
    _list1.append("-")
    a1 = str("")  # очищаем a1

def e_exp():
    global a1
    view.e1_action.insert(INSERT, "^")
    _list1.append("^")
    a1 = str("")  # очищаем a1

def square():
    global a1
    view.e1_action.insert(INSERT, "√()")
    left_cursor()
    _list1.append("√")
    if _list1[_list1.index("√") - 1] == "o": 
        del _list1[_list1.index("√") - 1]  # команда удаляет символ перед корнеи
    a1 = str("")  # очищаем a1

def e_exp_2():
    global a1
    view.e1_action.insert(INSERT, "^2")
    _list1.append("^2")
    if _list1[_list1.index("^2") - 1] == "o":
        del _list1[_list1.index("^2") - 1] 
    a1 = str("")  # очищаем a1

def e_sin():
    global a1
    view.e1_action.insert(INSERT, "sin()") # 
    left_cursor()
    _list1.append("sin")
    if _list1[_list1.index("sin") - 1] == "o":
        del _list1[_list1.index("sin") - 1]  # команда удаляет символ перед sin
    a1 = str("")  # очищаем a1

def e_log():
    global a1
    view.e1_action.insert(INSERT, "log()")
    left_cursor()
    _list1.append("log")
    if _list1[_list1.index("log") - 1] == "o":
        del _list1[_list1.index("log") - 1]  # команда удаляет символ перед log
    a1 = str("")  # очищаем a1

def e_cos():
    global a1
    view.e1_action.insert(INSERT, "cos()")
    left_cursor()
    _list1.append("cos")
    if _list1[_list1.index("cos") - 1] == "o":
        del _list1[_list1.index("cos") - 1]  # команда удаляет символ перед cos
    a1 = str("")  # очищаем a1

def e_ten_exp():
    global a1
    view.e1_action.insert(INSERT, "10^")
    _list1.append("10^")
    if _list1[_list1.index("10^") - 1] == "o":
        del _list1[_list1.index("10^") - 1] 
    a1 = str("")  # очищаем a1

def e_tg():
    global a1
    view.e1_action.insert(INSERT, "tg()")
    left_cursor()
    _list1.append("tg")
    if _list1[_list1.index("tg") - 1] == "o":
        del _list1[_list1.index("tg") - 1]  # команда удаляет символ перед tg
    a1 = str("")  # очищаем a1

def e_mod():
    global a1
    view.e1_action.insert(INSERT, "mod||")
    left_cursor()
    _list1.append("mod")
    if _list1[_list1.index("mod") - 1] == "o":
        del _list1[_list1.index("mod") - 1]  # команда удаляет символ перед tg
    a1 = str("")  # очищаем a1

def e_pi():
    global a1
    view.e1_action.insert(INSERT, "π")
    _list1.append("π")
    if _list1[_list1.index("π") - 1] == "o":
        del _list1[_list1.index("π") - 1]  # команда удаляет символ перед pi
    a1 = str("")  # очищаем a1

def e_factorial():
    global a1
    view.e1_action.insert(INSERT, "!")
    _list1.append("!")
    if _list1[_list1.index("!") - 1] == "o":
        del _list1[_list1.index("!") - 1]  # команда удаляет символ перед !
    a1 = str("")  # очищаем a1

def print_log(): # открываем окно с содержимым лог файла
    logger.print()
    
