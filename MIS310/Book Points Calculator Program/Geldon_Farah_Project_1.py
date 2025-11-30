import tkinter as tk

def compute_points():
    books = int(entry_books.get())
    if books == 0:
        points = 0
    elif books == 2:
        points = 5
    elif books == 4:
        points = 15
    elif books == 6:
        points = 30
    elif books >= 8:
        points = 60
    else:
        points = 0
    result_label.config(text=f"POINTS AWARDED: {points}")

window = tk.Tk()
window.title("book points")
window.geometry("300x200")

label_instruction = tk.Label(window, text="enter number of books purchased:")
label_instruction.pack(pady=5)

entry_books = tk.Entry(window)
entry_books.pack(pady=5)

btn_compute = tk.Button(window, text="compute points", command=compute_points)
btn_compute.pack(pady=5)

result_label = tk.Label(window, text="")
result_label.pack(pady=5)

window.mainloop()
