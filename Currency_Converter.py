from currency_converter import CurrencyConverter
import tkinter as tk
c=CurrencyConverter()

window=tk.Tk()
window.geometry("500x360")
window.title("Currency Converter")

def convert():
    amount=int(entry1.get())
    cur1=entry2.get()
    cur2=entry3.get()
    data=c.convert(amount,cur1,cur2)
    label4=tk.Label(window,text=data,font="Arial 16 italic").place(x=200,y=300)

label=tk.Label(window,text="Currency Converter",font="Arial 20 bold").pack()

label1=tk.Label(window,text="Enter the amount: ",font="Arial 16 bold").place(x=70,y=100)
entry1=tk.Entry(window)

label2=tk.Label(window,text="Enter your currency: ",font="Arial 16 bold").place(x=40,y=150)
entry2=tk.Entry(window)

label3=tk.Label(window,text="Enter desired currency: ",font="Arial 16 bold").place(x=15,y=200)
entry3=tk.Entry(window)


button=tk.Button(window,text="Convert",font="Arial 16 bold",command=convert).place(x=220,y=250)
entry1.place(x=270,y=105)
entry2.place(x=270,y=155)
entry3.place(x=270,y=205)
window.mainloop()

