import math
from tkinter import *
import logger
import view

def math_actions(list3):   # выполняются мат функции в след порядке: степени, триг функции, log, *, /, -, +

    count_mult = list3.count("*") # количество знаков "*" в списке
    count_div = list3.count("/") # количество знаков "/" в списке
    count_sum = list3.count("+") # количество знаков "+" в списке
    count_minus = list3.count("-") # количество знаков "-" в списке
    count_exp = list3.count("^") # количество встречающихся степеней в списке
    count_square = list3.count("√") # количество встречающихся кв корней в списке
    count_exp_2 = list3.count("^2")
    count_sin = list3.count("sin")
    count_log = list3.count("log")
    count_cos = list3.count("cos")
    count_tg = list3.count("tg")
    count_ten_exp = list3.count("10^")
    count_mod = list3.count("mod")
    count_factorial = list3.count("!")

    for i in range(len(list3)): # перебираю список чисел и действий в поиске нужного действия
        if list3[i] == "^":
            a = math.pow(float(list3[i - 1]), float(list3[i + 1]))  
            del list3[i - 1:i + 2] 
            list3.insert(i - 1, a) 
            count_exp -= 1 
            if count_exp == 0:
                break

    for i in range(len(list3)): # перебираю список чисел и действий в поиске нужного действия
        if list3[i] == "^2":
            a = math.pow(float(list3[i - 1]), 2) 
            del list3[i - 1:i + 1] 
            list3.insert(i - 1, a)
            count_exp_2 -= 1 
            if count_exp_2 == 0:
                break

    for i in range(len(list3)): # перебираю список чисел и действий в поиске нужного действия
        if list3[i] == "10^":
            a = math.pow(10, float(list3[i + 1]))
            del list3[i:i + 2] 
            list3.insert(i, a) 
            count_ten_exp -= 1 
            if count_ten_exp == 0:
                break

    for i in range(len(list3)): # перебираю список чисел и действий в поиске нужного действия
        if list3[i] == "√":
            a = math.sqrt(float(list3[i + 1])) 
            del list3[i:i + 2] 
            list3.insert(i, a) 
            count_square -= 1 
            if count_square == 0:
                break

    for i in range(len(list3)): # перебираю список чисел и действий в поиске нужного действия
        if list3[i] == "sin":
            print(list3[i])
            print(list3[i+1])
            print(math.sin(int(list3[i + 1])))
            a = math.sin(int(list3[i + 1])) 
            del list3[i:i + 2]
            list3.insert(i, a)
            count_sin -= 1 # счетчик количества действия sin
            if count_sin == 0:
                break

    for i in range(len(list3)): # перебираю список чисел и действий в поиске нужного действия
        if list3[i] == "log":
            a = math.log(float(list3[i + 1])) 
            del list3[i:i + 2]
            list3.insert(i, a)
            count_log -= 1 # счетчик количества действия log
            if count_log == 0:
                break

    for i in range(len(list3)): # перебираю список чисел и действий в поиске нужного действия
        if list3[i] == "cos":
            a = math.cos(float(list3[i + 1]))
            del list3[i:i + 2] 
            list3.insert(i, a) 
            count_cos -= 1 # счетчик количества действия cos
            if count_cos == 0:
                break

    for i in range(len(list3)): # перебираю список чисел и действий в поиске нужного действия
        if list3[i] == "tg":
            a = math.tan(float(list3[i + 1]))
            del list3[i:i + 2] 
            list3.insert(i, a) 
            count_tg -= 1 # счетчик количества действия tg
            if count_tg == 0:
                break

    for i in range(len(list3)): # перебираю список чисел и действий в поиске нужного действия
        if list3[i] == "mod":
            a = math.fabs(float(list3[i + 1]))
            del list3[i:i + 2] 
            list3.insert(i - 1, a) 
            count_mod -= 1 
            if count_mod == 0:
                break

    for i in range(len(list3)): # перебираю список чисел и действий в поиске пи
        if list3[i] == "π":
            list3[i] = math.pi

    for i in range(len(list3)): # перебираю список чисел и действий в поиске нужного действия
        if list3[i] == "!":
            a = math.factorial(int(list3[i - 1])) 
            del list3[i - 1:i + 1] 
            list3.insert(i - 1, a)
            count_factorial -= 1 
            if count_factorial == 0:
                break

    counter = len(list3)
    i = 0
    while counter >= 1:
        if list3[i] == "*":
            a = float(list3[i - 1]) * float(list3[i + 1]) # выполняю умножение элементов слева и справа от знака умножить, результат в а
            del list3[i - 1:i + 2] # удаляю умноженные элементы из списка
            list3.insert(i - 1, a) # и добавляю полученное произведение в начало списка
            i = i - 1
            count_mult = count_mult - 1 # счетчик количества умножений
            if count_mult == 0:
                break
        i = i + 1
        counter = counter - 1

    counter = len(list3)
    i = 0
    while counter >= 1:
        if list3[i] == "/":
            a = float(list3[i - 1]) / float(list3[i + 1]) # выполняю деление элемента слева от знака деление на элемент справа от зн дел, результат в а
            del list3[i - 1:i + 2] # удаляю делимое и делитель из списка
            list3.insert(i - 1, a) # и добавляю полученный результат в начало списка
            i = i - 1
            count_div = count_div - 1 # счетчик количества делений
            if count_div == 0:
                break
        i = i + 1
        counter = counter - 1

    counter = len(list3)
    i = 0
    while counter >= 1:
        if list3[i] == "-":
            a = float(list3[i - 1]) - float(list3[i + 1]) # выполняю вычитание элементов, результат в а
            del list3[i - 1:i + 2] # удаляю элементы из которого вычитали и вычитаемое из списка
            list3.insert(i - 1, a) # и добавляю полученную разницу в начало списка
            i = i - 1
            count_minus = count_minus - 1 # счетчик количества вычитаний
            if count_minus == 0:
                break
        i = i + 1
        counter = counter - 1

    counter = len(list3)
    i = 0
    while counter >= 1:
        if list3[i] == "+":
            a = float(list3[i - 1]) + float(list3[i + 1]) # выполняю сложение элементов слева и справа от знака +, результат в а
            del list3[i - 1:i + 2] # удаляю сложенные элементы из списка
            list3.insert(i - 1, a) # и добавляю полученную сумму в начало списка
            i = i - 1
            count_sum = count_sum - 1 # счетчик количества сложений
            if count_sum == 0:
                break
        i = i + 1
        counter = counter - 1
    return list3

def brackets(list1): # выполняет действия в скобках (находим первую правую скобку и выполняем действия слева от нее, удаляем эти скобки и переходим к следующей паре скобок)
    counter = len(list1)
    _list3 = []
    i = 0
    c = int(0)
    if list1.count("(")  == 0:
        math_actions(list1)

    elif list1.count("(") != list1.count(")"): # если не хватает скобки, выводит сообщение "Не хватает скобки"
        mistake_entry = Tk()
        mistake_entry.title("Сообщение")
        mistake_entry.geometry("300x30+1200+400")
        label = Label(mistake_entry, text = "Не хватает скобки", font=("Arial", 12))
        label.pack()
        mistake_entry.mainloop()

    else:
        while counter >= 1:
            if list1[i] == "(":
                c = i                           # запоминаем индекс последней левой скобки "("" перед первой правой скобкой ")" в списке. с - индекс
            if list1[i] == ")":                 # i - индекс первой правой скобки ")" в списке.
                    for j in range(i - c - 1):  # в промежутке между с и i выполняем функ. math_actions(_list3)
                        _list3.append(list1[c + 1 + j]) # в пустой список _list3 записываем содержимое скобок
                    a = math_actions(_list3)    # отправляем _list3 в функцию math_actions() для выполнения мат действий внутри скобок
                    del list1[c:i + 1]          # удаляю  элементы с индексами от с до i из списка list1
                    list1.insert(c, str(a[0]))  # добавляем результат полученный после math_actions() в список list1
                    _list3 = []
                    c = 0                       # обнуляю с и i
                    i = -1
                    counter = len(list1) + 1    # обновляю счетчик
            i = i + 1       
            counter = counter - 1
        
        if list1.count("(") == 0:
            math_actions(list1)

    logger.log("результат:{}".format(list1[0]))

    view.e2_result.insert(0, round(float(str(list1[0])), 4))

    


