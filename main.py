from tkinter import *
from tkinter import ttk
import calculate


# ---------------- Insert rows --------------------
def add_recordA():
    try:
        answerA.config(text='')
        float(valueInputA.get())
        value_sum_a = calculate.add_records(valueInputA.get(), descriptionInputA.get(), "A")
        treeA.insert(parent='', index='end', text="", values=(valueInputA.get(), descriptionInputA.get()))
        valueInputA.delete(0, END)
        descriptionInputA.delete(0, END)
        sumLabelA.config(text='Sum = '+value_sum_a + ' PLN')
    except ValueError:
        answerA.config(text='Please insert number')


def add_recordB():
    try:
        answerB.config(text='')
        float(valueInputB.get())
        value_sum_b = calculate.add_records(valueInputB.get(), descriptionInputB.get(), "B")
        treeB.insert(parent='', index='end', text="", values=(valueInputB.get(), descriptionInputB.get()))
        valueInputB.delete(0, END)
        descriptionInputB.delete(0, END)
        sumLabelB.config(text='Sum = ' + value_sum_b + ' PLN')
    except ValueError:
        answerB.config(text='Please insert number')


# ---------------- Remove rows --------------------
def remove_records():
    a = treeA.selection()
    b = treeB.selection()

    if len(a) > 0:
        for record_a in a:
            treeA.delete(record_a)
            print(treeA.item(record_a))
            value_sum_a = calculate.remove_record(record_a, "A")
            sumLabelA.config(text='Sum = ' + value_sum_a + ' PLN')
    elif len(b) > 0:
        for record_b in b:
            treeB.delete(record_b)
            value_sum_b = calculate.remove_record(record_b, "B")
            sumLabelB.config(text='Sum = ' + value_sum_b + ' PLN')


# ----------------- Root ----------------------------------
root = Tk()
root.geometry('960x500')
root.title('Bills_2.0')

style = ttk.Style()
style.theme_use('default')
style.configure("Treewiev", background="#D3D3D3", foregound="black", rowheight=25, fieldbackground="D3D3D3")
style.map("Treewiev", background=[('selected', "#347083")])

# ------------------ Frames -------------------------------
frameA = LabelFrame(root, text="Beti", padx=5, pady=5)
frameB = LabelFrame(root, text='Radek', padx=5, pady=5)

frameA.grid(row=0, column=0, padx=10, pady=10)
frameB.grid(row=0, column=1, padx=10, pady=10)

# ------------------- Labels -------------------------------
valueALabel = Label(frameA, text="Value")
nameALabel = Label(frameA, text="Name")
valueBLabel = Label(frameB, text="Value")
nameBLabel = Label(frameB, text="Name")

valueALabel.grid(row=0, column=0)
nameALabel.grid(row=0, column=1)
valueBLabel.grid(row=0, column=0)
nameBLabel.grid(row=0, column=1)

# ------------------- Input Fields --------------------------
valueInputA = Entry(frameA, width=10)
valueInputA.focus()
descriptionInputA = Entry(frameA, width=30)
valueInputB = Entry(frameB, width=10)
descriptionInputB = Entry(frameB, width=30)

valueInputA.grid(row=1, column=0)
descriptionInputA.grid(row=1, column=1, padx=5)
valueInputB.grid(row=1, column=0)
descriptionInputB.grid(row=1, column=1, padx=5)

# ------------------- Treeview of values ---------------------
columns = ('values', 'names')

treeA = ttk.Treeview(frameA, columns=columns, show='headings')
treeA.heading('values', text='Values')
treeA.heading('names', text='Name')

treeB = ttk.Treeview(frameB, columns=columns, show='headings')
treeB.heading('values', text='Values')
treeB.heading('names', text='Name')

treeA.grid(row=2, columnspan=3, sticky='nsew')
treeB.grid(row=2, columnspan=3, sticky='nsew')

# add a scrollbar  A -----
scrollbar = ttk.Scrollbar(frameA, orient=VERTICAL, command=treeA.yview)
treeA.configure(yscroll=scrollbar.set)
scrollbar.grid(row=2, column=3, sticky='ns')
# add a scrollbar  B -----
scrollbar = ttk.Scrollbar(frameB, orient=VERTICAL, command=treeB.yview)
treeB.configure(yscroll=scrollbar.set)
scrollbar.grid(row=2, column=3, sticky='ns')

# ------------------- Input field button --------------------
inputButtonA = Button(frameA, text="Enter", command=add_recordA)
inputButtonB = Button(frameB, text="Enter", command=add_recordB)

inputButtonA.grid(row=1, column=2)
inputButtonB.grid(row=1, column=2)

# -------------------SUM Label ------------------------------
sumLabelA = Label(frameA, text='')
sumLabelA.grid(row=4, column=0)

sumLabelB = Label(frameB, text='')
sumLabelB.grid(row=4, column=0)


# ------------------- Error message -------------------------
answerA = Label(frameA, fg="red", text='')
answerA.grid(row=5, column=1)

answerB = Label(frameB, fg="red", text='')
answerB.grid(row=5, column=1)

# -------------------- Remove records button ------------------
removeButton = Button(root, text="Remove record", command=remove_records)
removeButton.grid(row=1, columnspan=2)

root.mainloop()
