import tkinter as tk
from tkinter import ttk
from calendar import monthrange, month_name

root = tk.Tk()
root.title("Calendar")

year_var = tk.StringVar()
year_var.set(str(2023))
year_entry = ttk.Entry(root, textvariable=year_var, width=5)
year_entry.pack()

month_var = ttk.Combobox(root, values=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], state="readonly")
month_var.pack()
month_var.current(6)

month_label = tk.Label(root, text="", font=("Helvetica", 16, "bold"))
month_label.pack()

def update_calendar():
    year = int(year_var.get())
    month = month_var.current() + 1

    month_label.config(text=f"{month_name[month]} {year}")

    # Clear the existing calendar
    for widget in day_labels:
        widget.grid_forget()
    
    # Calculate the number of days in the selected month and the day of the week of the 1st day
    _, days_in_month = monthrange(year, month)
    first_day_of_month = monthrange(year, month)[0]
    
    # Generate the calendar grid
    row = 2
    col = first_day_of_month
    for day in range(1, days_in_month + 1):
        day_label = tk.Label(date_frame, text=str(day), font=("Helvetica", 12, "bold"))
        day_label.grid(row=row, column=col, padx=5, pady=5)
        day_labels.append(day_label)
        
        col += 1
        if col == 7:
            col = 0
            row += 1

# Update calendar when the "Go" button is clicked
go_button = ttk.Button(root, text="Go", command=update_calendar)
go_button.pack()

# Frame for day names
day_frame = tk.Frame(root)
day_frame.pack()

# Day labels (Mon, Tue, ..., Sun)
days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
for i, day in enumerate(days_of_week):
    day_label = tk.Label(day_frame, text=day, font=("Helvetica", 12, "bold"))
    day_label.grid(row=0, column=i, padx=5, pady=5)

# Frame for dates
date_frame = tk.Frame(root)
date_frame.pack()

# List to keep track of day labels
day_labels = []

# Initial calendar display
update_calendar()

root.mainloop()
