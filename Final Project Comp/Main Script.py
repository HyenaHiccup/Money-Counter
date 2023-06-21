import os
import datetime
from tkinter import Tk, Label, Entry, Button
from tkinter import ttk

# Set the file path to store the spending data
DATA_FILE = "spending.txt"

# Check if the data file exists, create it if not
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as file:
        file.write("Date,Amount\n")

def add_spending():
    # Get today's date
    today = datetime.date.today().strftime("%Y-%m-%d")

    # Get the amount from the entry field
    amount = float(entry_amount.get())

    # Open the data file in append mode and write the spending entry
    with open(DATA_FILE, "a") as file:
        file.write(f"{today},{amount}\n")

    # Clear the entry field
    entry_amount.delete(0, "end")

def show_spending():
    # Read the spending data from the file
    with open(DATA_FILE, "r") as file:
        data = file.readlines()

    # Create a new window to display the spending data
    window = Tk()
    window.title("Spending Tracker")

    # Set pink theme for the window
    window.configure(bg="#FFC0CB")

    # Create a treeview to display the spending entries
    treeview = ttk.Treeview(window, columns=("Date", "Amount"), show="headings")
    treeview.heading("Date", text="Date")
    treeview.heading("Amount", text="Amount")
    treeview.pack(padx=10, pady=10)

    for entry in data[1:]:
        date, amount = entry.strip().split(",")
        treeview.insert("", "end", values=(date, f"${amount}"))

    # Calculate the total spending
    total_spending = sum(float(entry.strip().split(",")[1]) for entry in data[1:])
    Label(window, text="Total spending:", font=("Arial", 12, "bold"), bg="#FFC0CB").pack(pady=5)
    Label(window, text=f"${total_spending:.2f}", font=("Arial", 12, "bold"), bg="#FFC0CB").pack()

    # Run the Tkinter event loop
    window.mainloop()

# Create the main window
root = Tk()
root.title("Daily Spending Tracker")

# Set pink theme for the window
root.configure(bg="#FFC0CB")

# Create labels and entry fields
Label(root, text="Spending Amount: $", font=("Arial", 12), bg="#FFC0CB").grid(row=0, column=0, padx=10, pady=5)
entry_amount = Entry(root, font=("Arial", 12))
entry_amount.grid(row=0, column=1, padx=10, pady=5)

# Create buttons with pink aesthetic
Button(root, text="Add Spending", font=("Arial", 12), bg="#FF69B4", fg="white", command=add_spending).grid(row=1, column=0, padx=10, pady=5)
Button(root, text="Show Spending", font=("Arial", 12), bg="#FF69B4", fg="white", command=show_spending).grid(row=1, column=1, padx=10, pady=5)

# Run the Tkinter event loop
root.mainloop()
