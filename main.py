import tkinter

window = tkinter.Tk()
window.title("Мой калькулятор")
window.geometry("300x300")

def add():
    print("Выполняю сложение")
    number1 = text_num1.get()
    number1 = int(number1)
    print(number1)
    number2 = text_num2.get()
    number2 = int(number2)
    print(number2)
    result = number1 + number2
    print(result)
    text_answer.delete(0,"end")
    text_answer.insert(0, f"{number1} + {number2} = {result}")

def sub():
    print("Выполняю вычетание")
    number1 = text_num1.get()
    number1 = int(number1)
    print(number1)
    number2 = text_num2.get()
    number2 = int(number2)
    print(number2)
    result = number1 - number2
    print(result)
    text_answer.delete(0, "end")
    text_answer.insert(0, f"{number1} - {number2} = {result}")

def mul():
    print("Выполняю умножение")
    number1 = text_num1.get()
    number1 = int(number1)
    print(number1)
    number2 = text_num2.get()
    number2 = int(number2)
    print(number2)
    result = number1 * number2
    print(result)
    text_answer.delete(0, "end")
    text_answer.insert(0, f"{number1} * {number2} = {result}")

def div():
    print("Выполняю деление")
    number1 = text_num1.get()
    number1 = int(number1)
    print(number1)
    number2 = text_num2.get()
    number2 = int(number2)
    print(number2)
    result = number1 / number2
    print(result)
    text_answer.delete(0, "end")
    text_answer.insert(0, f"{number1} / {number2} = {result}")


button_add = tkinter.Button(window, text = "+", command  = add)
button_add.place(x = 95, y = 110)

button_sub = tkinter.Button(window, text = "-", command = sub)
button_sub.place(x = 160, y = 110)

button_mul = tkinter.Button(window, text = "*", command = mul)
button_mul.place(x = 95, y = 154)

button_div = tkinter.Button(window, text = ":", command = div)
button_div.place(x = 160, y = 154)

#button_equals = tkinter.Button(window, text = "=")
#button_equals.place(x = 130, y = 180 )

text_num1 = tkinter.Entry(window, width = 20)
text_num1.place(x = 95, y = 40)

text_num2 = tkinter.Entry(window, width = 20)
text_num2.place(x = 95, y = 81)

text_answer = tkinter.Entry(window, width = 20)
text_answer.place(x = 95, y = 221)


window.mainloop()
