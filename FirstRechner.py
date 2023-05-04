from tkinter import *

window = Tk()
window.title("Rechner")
window.geometry('600x600+700+100')


def input_into_entry(symbol):
    entry.insert(END, symbol)

def clear():
    entry.delete(0, END)

def count_result():
    text = entry.get()
    result = 0
    if "+" in text:
        splitted_text = text.split("+")
        first = float(splitted_text[0])
        second = float(splitted_text[1])
        result = first + second
    if "-" in text:
        splitted_text = text.split("-")
        first = float(splitted_text[0])
        second = float(splitted_text[1])
        result = first - second
    if "/" in text:
        splitted_text = text.split("/")
        first = float(splitted_text[0])
        second = float(splitted_text[1])
        result = first / second
    if "*" in text:
        splitted_text = text.split("*")
        first = float(splitted_text[0])
        second = float(splitted_text[1])
        result = first * second
    clear()   
    entry.insert(0, result)    


entry = Entry(window, width = 25, font = ("", 25))
entry.place(x = 100, y= 45)


btn1 = Button(window, bg= "black", fg="white", text='1', command = lambda : input_into_entry("1"))
btn1.place(x = 100, y=100, width = 50, height = 50)

btn1 = Button(window, bg= "black", fg="white", text='2', command = lambda : input_into_entry("2"))
btn1.place(x = 150, y=100, width = 50, height = 50)

btn1 = Button(window, bg= "black", fg="white", text='3', command = lambda : input_into_entry("3"))
btn1.place(x = 200, y=100, width = 50, height = 50)

btn1 = Button(window, bg= "black", fg="white", text='+', command = lambda : input_into_entry("+"))
btn1.place(x = 250, y=100, width = 50, height = 50)

btn1 = Button(window, bg= "black", fg="white", text='4', command = lambda : input_into_entry("4"))
btn1.place(x = 100, y=150, width = 50, height = 50)

btn1 = Button(window, bg= "black", fg="white", text='5', command = lambda : input_into_entry("5"))
btn1.place(x = 150, y=150, width = 50, height = 50)

btn1 = Button(window, bg= "black", fg="white", text='6', command = lambda : input_into_entry("6"))
btn1.place(x = 200, y=150, width = 50, height = 50)

btn1 = Button(window, bg= "black", fg="white", text='-', command = lambda : input_into_entry("-"))
btn1.place(x = 250, y=150, width = 50, height = 50)

btn1 = Button(window, bg= "black", fg="white", text='7', command = lambda : input_into_entry("7"))
btn1.place(x = 100, y=200, width = 50, height = 50)

btn1 = Button(window, bg= "black", fg="white", text='8', command = lambda : input_into_entry("8"))
btn1.place(x = 150, y=200, width = 50, height = 50)

btn1 = Button(window, bg= "black", fg="white", text='9', command = lambda : input_into_entry("9"))
btn1.place(x = 200, y=200, width = 50, height = 50)

btn1 = Button(window, bg= "black", fg="white", text='/', command = lambda : input_into_entry("/"))
btn1.place(x = 250, y=200, width = 50, height = 50)

btn1 = Button(window, bg= "black", fg="white", text='.', command = lambda : input_into_entry("."))
btn1.place(x = 100, y=250, width = 50, height = 50)

btn1 = Button(window, bg= "black", fg="white", text='CE', command = clear)
btn1.place(x = 150, y=250, width = 50, height = 50)

btn1 = Button(window, bg= "black", fg="white", text='=', command = count_result)
btn1.place(x = 200, y=250, width = 50, height = 50)

btn1 = Button(window, bg= "black", fg="white", text='*')
btn1.place(x = 250, y=250, width = 50, height = 50)

btn1 = Button(window, bg= "black", fg="white", text='0', command = lambda : input_into_entry("0"))
btn1.place(x = 300, y=250, width = 50, height = 50)




window.mainloop()