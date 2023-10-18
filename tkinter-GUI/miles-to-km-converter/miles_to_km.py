from tkinter import *

window = Tk()
window.title("Mile To Km Converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=10)
miles_input.grid(row=1, column=5)

miles_label = Label(text="Miles")
miles_label.config(padx=5)
miles_label.grid(row=1, column=6)

result_label = Label(text=f"is 0 Km")
result_label.config(pady=10)
result_label.grid(row=2, column=5)

def btn_clicked():
    result = float(miles_input.get()) * 1.609
    result_label.config(text=f"is {result} Km")

calc_btn = Button(text="Calculate", command=btn_clicked)
calc_btn.grid(row=3, column=5)








window.mainloop()