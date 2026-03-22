from tkinter import *

notes = []


def add_note():
    notes.append(entry.get())
    entry.delete(0, END)
    print(notes)


def save_notes():
    global notes
    with open("line_by_line_notes.txt", "a+") as file:
        for note in notes:
            file.write(f"{note}\n")
        notes = []
        entry.delete(0, END)



def save_and_close():
    save_notes()
    root.destroy()


def preview_notes():
    global notes
    label2 = Label(root, text="*** Preview (remember to save notes!) ***", width=60)
    label2.grid(row=4, column=0, columnspan=3, padx=10, pady=10)
    for i in range(len(notes)):
        label = Label(root, text=notes[i-1], width=60)
        label.grid(row=i+4, column=0, columnspan=3, padx=10, pady=10)


root = Tk()

root.title("*** Line by line notebook ***")
# root.geometry("500x100")

label1 = Label(root, text="*** Line by line notebook ***", width=60)
label1.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

entry = Entry(root, width=60)
entry.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

add_btn = Button(root, text="*** Add new Line ***", command=add_note, width=20)
add_btn.grid(row=2, column=0)

save_btn = Button(root, text="*** Save nad continue ***", command=save_notes, width=20)
save_btn.grid(row=2, column=1)

close_btn = Button(root, text="*** Close and save ***", command=save_and_close, width=20)
close_btn.grid(row=2, column=2)

preview_btn = Button(root, text="*** Preview Notes***", command=preview_notes, width=60)
preview_btn.grid(row=3, column=0, columnspan=3, padx=10, pady=10)





root.mainloop()