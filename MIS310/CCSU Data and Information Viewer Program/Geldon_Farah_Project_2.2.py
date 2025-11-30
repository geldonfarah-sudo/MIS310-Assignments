from tkinter import *
from PIL import ImageTk, Image
import pandas as pd


root = Tk()
root.title("CCSU App")
root.geometry("780x560")
root.resizable(0, 0)

bg_blue = "#9bb8dc"
btn_blue = "#1b3b7a"
btn_blue_active = "#0f2853"
txt_white = "white"

root.configure(bg=bg_blue)


logo_img = Image.open("logo2.png")
try:
    logo_img = logo_img.resize((110, 110), Image.Resampling.LANCZOS)
except AttributeError:
    logo_img = logo_img.resize((110, 110), Image.ANTIALIAS)
logo_img = logo_img.convert("RGBA")
pix = logo_img.getdata()
new_pix = []
for p in pix:
    if p[:3] == (255, 255, 255):
        new_pix.append((255, 255, 255, 0))
    else:
        new_pix.append(p)
logo_img.putdata(new_pix)
logo_photo = ImageTk.PhotoImage(logo_img)
Label(root, image=logo_photo, bg=bg_blue).place(x=12, y=12)


data = pd.read_csv("midterm_exam.csv")


lb = Label(root, justify="left", anchor="nw", bg=bg_blue, fg="black", font=("arial", 11))
lb.place(x=24, y=190, width=732, height=340)

def show(text):
    lb.config(text=text)


def calendar():
    df = pd.DataFrame(data, columns=["CalendarDate"])
    selected = df[~df["CalendarDate"].isnull()]
    show(selected.to_string(index=False))

def buildings():
    df = pd.DataFrame(data, columns=["Buildings"])
    selected = df[~df["Buildings"].isnull()]
    show(selected.to_string(index=False))

def faculty():
    df = pd.DataFrame(data, columns=["FacultyName"])
    selected = df[~df["FacultyName"].isnull()]
    show(selected.to_string(index=False))

def school_of_business():
    items = [
        "Accounting",
        "Finance",
        "Management & Organization",
        "Marketing",
        "Management Information Systems (MIS)",
        "Business Analytics"
    ]
    show("School of Business:\n- " + "\n- ".join(items))

def mis_department():
    items = [
        "Intro to MIS",
        "Databases Management",
        "Systems Analysis & Design",
        "Business Analytics / Data Visualization",
        "Network and Information Security",
        "Project Management"
    ]
    show("MIS Department:\n- " + "\n- ".join(items))


def make_btn(parent, text, cmd):
    wrapper = Frame(parent, bg=btn_blue)
    lbl = Label(wrapper, text=text, bg=btn_blue, fg=txt_white,
                font=("arial", 10, "bold"), padx=12, pady=6)
    lbl.pack()
    def on_click(e=None): cmd()
    def on_enter(e): lbl.config(bg=btn_blue_active)
    def on_leave(e): lbl.config(bg=btn_blue)
    lbl.bind("<Button-1>", on_click)
    lbl.bind("<Enter>", on_enter)
    lbl.bind("<Leave>", on_leave)
    return wrapper


btn_frame = Frame(root, bg=bg_blue)
btn_frame.place(x=110, y=46)

make_btn(btn_frame, "Calendar", calendar).pack(side="left", padx=8)
make_btn(btn_frame, "Buildings", buildings).pack(side="left", padx=8)
make_btn(btn_frame, "Faculty", faculty).pack(side="left", padx=8)
make_btn(btn_frame, "School of Business", school_of_business).pack(side="left", padx=8)
make_btn(btn_frame, "MIS Department", mis_department).pack(side="left", padx=8)

root.mainloop()


