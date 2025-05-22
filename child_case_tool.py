
import tkinter as tk
from tkinter import messagebox
import pandas as pd
import pyperclip
import os

# Read the data file path from config.txt
def get_data_path():
    config_path = 'config.txt'
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            return f.read().strip()
    else:
        return 'sample_cases.csv'  # fallback if config.txt doesn't exist

data_file = get_data_path()

# Try to load the CSV file
try:
    df = pd.read_csv(data_file, dtype={'parent_case_id': str})
except FileNotFoundError:
    df = pd.DataFrame(columns=[
        'parent_case_id', 'subject', 'event_edition',
        'contact_name', 'contact_email', 'contact_phone', 'company_name'
    ])
    messagebox.showerror("File Not Found", f"The data file could not be found:\n\n{data_file}\n\nPlease check your config.txt or make sure OneDrive is syncing.")

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

    cleaned_input = case_id.replace("#", "").strip()
    df['parent_case_id'] = df['parent_case_id'].astype(str).str.replace("#", "").str.strip()
    match = df[df['parent_case_id'] == cleaned_input]

    result_frame.pack(pady=10)

    if not match.empty:
        record = match.iloc[0]

        def add_clickable(row, label, text):
            label_widget = tk.Label(result_frame, text=label, anchor='w', bg='white', fg='black')
            label_widget.grid(row=row, column=0, sticky='w', padx=10, pady=2)
            value = tk.Label(result_frame, text=text, fg='black', cursor='hand2',
                            font=('Arial', 10, 'bold'), bg='white')
            value.bind("<Button-1>", lambda e: copy_to_clipboard(text))
            value.grid(row=row, column=1, sticky='w', padx=10, pady=2)

        row = 0
        add_clickable(row, "Parent Case ID:", record['parent_case_id']); row += 1
        add_clickable(row, "Subject:", record['subject']); row += 1
        add_clickable(row, "Event Edition:", record['event_edition']); row += 1
        add_clickable(row, "Contact Name:", record['contact_name']); row += 1
        add_clickable(row, "Contact Email:", record['contact_email']); row += 1
        add_clickable(row, "Contact Phone:", record['contact_phone']); row += 1
        add_clickable(row, "Company Name:", record['company_name'])

    else:
        tk.Label(result_frame, text=f"Parent Case ID {case_id}", font=('Arial', 10, 'bold'), bg='white', fg='black').pack()
        tk.Label(result_frame, text="No information found.\nThe entered Parent Case ID is not found in the database.",
                 fg='red', bg='white').pack()

# GUI setup
root = tk.Tk()
root.title("Child Case Lookup Tool")
root.geometry("450x500")
root.configure(bg='white')

search_frame = tk.Frame(root, bg='white')
search_frame.pack(pady=20)

search_entry = tk.Entry(search_frame, width=30, font=('Arial', 12))
search_entry.pack(side='left', padx=(0, 10))

search_btn = tk.Button(search_frame, text="Search", command=search_case)
search_btn.pack(side='left')

instruction_label = tk.Label(root,
    text="Enter the parent case ID to search for the customer details and case information.",
    wraplength=400, justify='left', bg='white', fg='black')
instruction_label.pack()

result_frame = tk.Frame(root, bg='white')
result_frame.pack()

root.mainloop()
