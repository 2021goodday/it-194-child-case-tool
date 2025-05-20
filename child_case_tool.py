
import tkinter as tk
from tkinter import messagebox
import pandas as pd
import pyperclip
import os

# Load data from CSV (make sure this file is in the same folder)
data_file = 'sample_cases.csv'

if os.path.exists(data_file):
    df = pd.read_csv(data_file)
else:
    df = pd.DataFrame(columns=['parent_case_id', 'date_opened', 'customer_name', 'email', 'phone', 'description'])

# Clipboard function
def copy_to_clipboard(text):
    pyperclip.copy(text)
    messagebox.showinfo("Copied", f"'{text}' copied to clipboard.")

# Search function
def search_case():
    case_id = search_entry.get().strip()
    result_frame.pack_forget()
    for widget in result_frame.winfo_children():
        widget.destroy()

    match = df[df['parent_case_id'].astype(str) == case_id]
    result_frame.pack(pady=10)

    if not match.empty:
        record = match.iloc[0]

        def add_clickable(label, text):
            label_widget = tk.Label(result_frame, text=label, anchor='w')
            label_widget.pack(fill='x', padx=10)
            value = tk.Label(result_frame, text=text, fg='blue', cursor='hand2', font=('Arial', 10, 'bold'))
            value.bind("<Button-1>", lambda e: copy_to_clipboard(text))
            value.pack(fill='x', padx=20)

        add_clickable("Parent Case ID:", record['parent_case_id'])
        tk.Label(result_frame, text=f"Date opened: {record['date_opened']}", anchor='w').pack(fill='x', padx=10, pady=(5, 10))
        add_clickable("Customer name:", record['customer_name'])
        add_clickable("Email:", record['email'])
        add_clickable("Phone number:", record['phone'])
        add_clickable("Case details and description:", record['description'])

    else:
        tk.Label(result_frame, text=f"Parent Case ID {case_id}", font=('Arial', 10, 'bold')).pack()
        tk.Label(result_frame, text="No information found.\nThe entered Parent Case ID is not found in the database.", fg='red').pack()

# GUI setup
root = tk.Tk()
root.title("Child Case Lookup Tool")
root.geometry("450x500")

search_frame = tk.Frame(root)
search_frame.pack(pady=20)

search_entry = tk.Entry(search_frame, width=30, font=('Arial', 12))
search_entry.pack(side='left', padx=(0, 10))

search_btn = tk.Button(search_frame, text="Search", command=search_case)
search_btn.pack(side='left')

instruction_label = tk.Label(root, text="Enter the parent case ID to search for the customer details and case information.", wraplength=400, justify='left')
instruction_label.pack()

result_frame = tk.Frame(root)
result_frame.pack()

root.mainloop()
