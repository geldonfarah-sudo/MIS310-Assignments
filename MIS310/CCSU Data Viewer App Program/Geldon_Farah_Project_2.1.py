from tkinter import *
from PIL import ImageTk, Image
import pandas as pd

root = Tk()
root.title("CCSU App")
root.geometry("720x520")
root.resizable(0, 0)
root.configure(bg='light blue')

img = Image.open('logo2.png')
try:
    img = img.resize((160, 160), Image.Resampling.LANCZOS)
except AttributeError:
    img = img.resize((140, 140), Image.ANTIALIAS)
img = img.convert("RGBA")
data = img.getdata()
newData = []
for item in data:
    if item[:3] == (255, 255, 255):
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)
img.putdata(newData)
img.save("transparent.png")

logo = Image.open("transparent.png")
logo = ImageTk.PhotoImage(logo)
logoLabel = Label(root, image=logo, bg='light blue')
logoLabel.place(x=10, y=10)

data = pd.read_csv("midterm_exam.csv")

lb = Label(root, justify="left", bg="light blue", anchor="nw", font=("arial", 11))
lb.place(x=20, y=200, width=680, height=300)

def clear_and_show(text):
    lb.config(text=text)

def calendar():
    df = pd.DataFrame(data, columns=['CalendarDate'])
    selected_rows = df[~df['CalendarDate'].isnull()]
    clear_and_show(selected_rows.to_string(index=False))

def building():
    df = pd.DataFrame(data, columns=['Buildings'])
    selected_rows = df[~df['Buildings'].isnull()]
    clear_and_show(selected_rows.to_string(index=False))

def faculty():
    df = pd.DataFrame(data, columns=['FacultyName'])
    selected_rows = df[~df['FacultyName'].isnull()]
    clear_and_show(selected_rows.to_string(index=False))

btn_frame = Frame(root, bg="light blue")
btn_frame.place(x=180, y=60)

button1 = Button(btn_frame, text='Calendar', command=calendar, bg="light green")
button1.pack(side="left", padx=10)

button2 = Button(btn_frame, text='Buildings', command=building, bg="light green")
button2.pack(side="left", padx=10)

button3 = Button(btn_frame, text='Faculty', command=faculty, bg="light green")
button3.pack(side="left", padx=10)

root.mainloop()






