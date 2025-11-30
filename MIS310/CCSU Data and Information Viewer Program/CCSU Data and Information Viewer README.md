CCSU Data and Information Viewer (Tkinter + Pandas)
Overview

This program builds a graphical interface that displays different types of CCSU-related information. Users can view items from a CSV file—such as calendar dates, buildings, and faculty names—or browse custom lists for the School of Business and the MIS Department. The interface includes a processed logo and styled buttons for cleaner presentation.

How It Works

The application loads a CCSU logo, removes its white background, and renders it on the window. A CSV file is read using Pandas, and specific columns can be displayed based on the user’s selection.
Five buttons control what appears in the output area:

Calendar

Buildings

Faculty

School of Business

MIS Department

Each button applies the appropriate logic:

For CSV-based options, a dataframe is filtered to remove empty rows.

For department lists, predefined items are shown.
Custom button widgets are created with hover effects to improve the interface.
