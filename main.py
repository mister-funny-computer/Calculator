import tkinter

window = tkinter.Tk()
window.title("Мой калькулятор")
window.geometry("300x300")

button_add = tkinter.Button(window, text = "+")
button_add.place(x = 95, y = 110)

button_sub = tkinter.Button(window, text = "-")
button_sub.place(x = 160, y = 110)

button_mul = tkinter.Button(window, text = "*")
button_mul.place(x = 95, y = 154)

button_div = tkinter.Button(window, text = ":")
button_div.place(x = 160, y = 154)

button_equals = tkinter.Button(window, text = "=")
button_equals.place(x = 130, y = 180 )

window.mainloop()
