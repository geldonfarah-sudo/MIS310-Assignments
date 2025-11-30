CCSU Data Viewer App (Tkinter + Pandas)
Overview

This program creates a graphical interface that displays selected information from a CSV file. The user can choose to view calendar dates, buildings, or faculty names by clicking one of the buttons in the window. The interface also includes a processed version of the CCSU logo with the white background made transparent.

How It Works

The program loads an image, removes its white background, and displays it in the upper corner of the window. It also reads data from midterm_exam.csv using Pandas.
Three buttons allow the user to display specific columns:

Calendar

Buildings

Faculty

Each button extracts the relevant column from the dataframe, removes empty rows, and shows the values inside a label widget. The layout uses Tkinter frames, labels, and buttons to organize everything on screen.
