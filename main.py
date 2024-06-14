from tkinter import *
import pickle
import joblib as jb
scaler = jb.load("scale.save")
pkl_filename = "pickle_mode.pkl"
with open(pkl_filename, 'rb') as file:
    pickle_model = pickle.load(file)
def clicked():
    test = [[float(txt_1.get()),float(txt_2.get()),float(txt_3.get()),float(txt_4.get()),float(txt_5.get()),float(txt_6.get()),float(txt_7.get()),float(txt_8.get()),float(txt_9.get()),]]
    print(test)
    pred = pickle_model.predict(test)
    print(pred)
    if pred[0] == 1:
        pred = "АЛАЯҚТЫҚ"
    else:
        pred = "ҚАЛЫПТЫ"
    lbl_10.configure(text=pred)
def delete():
    txt_1.delete(0, END)
    txt_2.delete(0, END)
    txt_3.delete(0, END)
    txt_4.delete(0, END)
    txt_5.delete(0, END)
    txt_6.delete(0, END)
    txt_7.delete(0, END)
    txt_8.delete(0, END)
    txt_9.delete(0, END)
    lbl_10.configure(text="")

window = Tk()
window.title("Fraud detection")
window.geometry('400x250')
lbl_1 = Label(window, text="Сумма")
lbl_1.grid(column=0, row=0)
txt_1 = Entry(window, width=10)
txt_1.grid(column=1, row=0)
lbl_2 = Label(window, text="Жынысы")
lbl_2.grid(column=0, row=1)
txt_2 = Entry(window, width=10)
txt_2.grid(column=1, row=1)
lbl_3 = Label(window, text="Индекс")
lbl_3.grid(column=0, row=2)
txt_3 = Entry(window, width=10)
txt_3.grid(column=1, row=2)
lbl_4 = Label(window, text="Ені")
lbl_4.grid(column=0, row=3)
txt_4 = Entry(window, width=10)
txt_4.grid(column=1, row=3)
lbl_5 = Label(window, text="Ұзақтығы")
lbl_5.grid(column=0, row=4)
txt_5 = Entry(window, width=10)
txt_5.grid(column=1, row=4)
lbl_6 = Label(window, text="Қала популяциясы")
lbl_6.grid(column=0, row=5)
txt_6 = Entry(window, width=10)
txt_6.grid(column=1, row=5)
lbl_7 = Label(window, text="Unix уақыты")
lbl_7.grid(column=0, row=6)
txt_7 = Entry(window, width=10)
txt_7.grid(column=1, row=6)
lbl_8 = Label(window, text="Сату кеңдігі")
lbl_8.grid(column=0, row=7)
txt_8 = Entry(window, width=10)
txt_8.grid(column=1, row=7)
lbl_9 = Label(window, text="Сату ұзақтығы")
lbl_9.grid(column=0, row=8)
txt_9 = Entry(window, width=10)
txt_9.grid(column=1, row=8)
btn = Button(window, text="ТЕКСЕРУ!", command=clicked)
btn.grid(column=2, row=0)
btn_1 = Button(window, text="ТАЗАЛАУ", command=delete)
btn_1.grid(column=0, row=9)
lbl_10 = Label(window, text="")
lbl_10.grid(column=2, row=1)
window.mainloop()