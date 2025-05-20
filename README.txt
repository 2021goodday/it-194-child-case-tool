
Child Case Lookup Tool - README
===============================

This tool helps you quickly retrieve customer and case information based on a Parent Case ID.
Each field is clickable, and clicking it will copy that specific value to your clipboard.

-------------------------------
CONTENTS
-------------------------------
1. Files Included
2. Requirements
3. How to Run the Tool
4. How to Convert to EXE
5. Notes

-------------------------------
1. Files Included
-------------------------------
- child_case_tool.py          → Python script for the tool
- sample_cases.csv            → Sample case data (replace with real data if needed)

-------------------------------
2. Requirements
-------------------------------
Make sure Python is installed on your computer.
You also need to install two libraries:
  > pip install pandas pyperclip

-------------------------------
3. How to Run the Tool
-------------------------------
- Place both files in the same folder.
- Open a terminal or command prompt.
- Navigate to that folder:
  > cd path/to/folder
- Run the tool:
  > python child_case_tool.py

-------------------------------
4. How to Convert to EXE
-------------------------------
To make the tool portable (no need to install Python on other computers):

1. Install pyinstaller:
  > pip install pyinstaller

2. Run the following command:
  > pyinstaller --onefile --noconsole child_case_tool.py

3. Your EXE file will be in the "dist" folder.

-------------------------------
5. Notes
-------------------------------
- Double-check that your CSV has the correct column names:
  parent_case_id, date_opened, customer_name, email, phone, description

- Update 'sample_cases.csv' with your actual case data.

- The tool will show a "Copied!" popup when a field is successfully copied.
