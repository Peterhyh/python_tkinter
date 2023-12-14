import tkinter

window = tkinter.Tk()
window.title("[TITLE HERE]")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="Title", font=("Ariel", 24, "italic"))
my_label.pack()

window.mainloop()
