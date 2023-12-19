import tkinter

window = tkinter.Tk()
window.title("My Program")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="Title", font=("Ariel", 25, "italic"))
my_label.grid(column=0, row=0)


def button_click():
    my_label.config(text=f"{entry.get()}")


button = tkinter.Button(text="Button", command=button_click)
button.grid(column=1, row=1)


new_button = tkinter.Button(text="New Button")
new_button.grid(column=2, row=0)


entry = tkinter.Entry(width=10)
entry.grid(column=3, row=2)


window.mainloop()
