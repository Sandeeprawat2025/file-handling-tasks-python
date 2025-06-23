# File Handling Tasks in Python

This repository contains Python scripts for completing two basic file handling tasks using the `with open()` context manager, error handling, and user interaction.

---

## ✅ Task 1: Read a File and Handle Errors

**Objective:**  
- Open and read a text file named `sample.txt`
- Print its content line by line
- Gracefully handle the case if the file does not exist

### 📄 Script: `read_sample_file.py`  
**Features:**
- Uses `try-except` block to handle `FileNotFoundError`
- Uses `enumerate()` to print each line with line numbers
- Output format matches expected assignment requirement

**Expected Output (if file exists):**
```
Reading file content:
Line 1: This is a sample text file.
Line 2: It contains multiple lines.
```

**Expected Output (if file does NOT exist):**
```
Error: The file 'sample.txt' was not found.
```

---

## ✅ Task 2: Write and Append Data to a File

**Objective:**  
- Accept user input and write it to a file named `output.txt`
- Accept additional input and append it to the same file
- Display the final contents of the file

### 📄 Script: `write_and_append_output.py`  
**Features:**
- Uses input prompts for dynamic content
- Writes using `'w'` mode and appends using `'a'` mode
- Reads final content using `'r'` mode

**Expected Output Example:**
```
Enter text to write to the file: Hello, Python!
Data successfully written to output.txt.

Enter additional text to append: Learning file handling in Python.
Data successfully appended.

Final content of output.txt:
Hello, Python!
Learning file handling in Python.
```

---

## 📁 Files Included
- `read_sample_file.py`
- `write_and_append_output.py`
- `README.md`

---

## 💡 Note
Ensure `sample.txt` exists in the same directory while testing Task 1, or test the error output.
