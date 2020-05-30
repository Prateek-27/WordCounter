import tkinter as tk
from tkinter import font

root = tk.Tk()
Height = 550
Width = 600

def countwords(text):
  #Counts the number of words in sentence s
  str_list = text.split(" ")
  s_len = len(str_list)
  output = "Number of words are " + str(s_len)
  return output


def countchar(text):
  #counts the number of characters in sentence s

  c_len = len(text)
  output = "Number of characters are " + str(c_len)
  return output

def arrange(text):
    w = countwords(text)
    c = countchar(text)
    wc = w + '\n' + c
    return wc

def result(text):
    lable2['text'] = arrange(text)



canvas = tk.Canvas(root, height=Height, width=Width)
canvas.pack()

frame1 = tk.Frame(root, bg='pink', bd=10)
frame1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.45)

label = tk.Label(frame1, text="Enter the text below", font=('Courier', 14),bg='Yellow')
label.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.1)

text = tk.Text(frame1, font=('Courier', 14))
text.place(relx=0.05, rely=0.20, relwidth=0.9, relheight=0.5)

button = tk.Button(frame1, text="Count", font=('Courier', 10), bg='white', fg='red', command=lambda: result(text.get(1.0 ,tk.END)))
button.place(relx=0.45, rely=0.75, relwidth=0.1, relheight=0.1)

frame2 = tk.Frame(root, bg='blue', bd=5)
frame2.place(relx=0.1, rely=0.55, relwidth=0.8, relheight=0.3)

lable2 = tk.Label(frame2, font=('Courier', 18))
lable2.place(relwidth=1, relheight=1)

root.mainloop()