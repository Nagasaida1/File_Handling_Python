# File_Handling_Python

## **Python Programs: File Reading & Writing**

### **Overview**
This repository contains two Python programs demonstrating file handling:

1. **Task 1: Read a File and Handle Errors**  
2. **Task 2: Write and Append Data to a File**  

Each program performs file operations and includes error handling.

---

## **Task 1: Read a File and Handle Errors**  
**Filename:** `Task1.py`  

### **Description**  
This program attempts to open and read a file named `sample.txt`. If the file exists, it prints the content line by line. If the file is missing, it displays an error message.

### **Usage**  
Run the script and ensure `sample.txt` exists in the same directory. If the file is missing, an error will be displayed.

### **Example Output**  
```d
Reading file Content:
Line 1: It contains multiple lines of text.
Line 2: Python is great for file handling!
```
### **If the file does not exist:**
```d
Error: The file 'sample.txt' was not found.
```

---

## **Task 2: Write and Append Data to a File**  
**Filename:** `Task2.py`  

### **Description**  
This program allows the user to write text to a file (`output.txt`), append additional data, and then display the final content of the file.

### **Usage**  
Run the script and enter text when prompted. The program will save the input, append more text, and finally print the file contents.

### **Example Output**  
```d
Enter text to write to the file: Hello, python!
Data successfully written to output.txt.
Enter additional text to append: Learing file handling in python.
Data successfully appended. 

Final content of output.txt:
Hello, python!
Learing file handling in python.
```

---

## **How to Run the Programs**
1. Ensure Python is installed on your system.  
2. Clone this repository or download the files.  
3. Open a terminal/command prompt and navigate to the directory where the files are located.  
4. Run the programs using the following commands:

   - **For Task 1:**  
     ```
     python Task1.py
     ```
   - **For Task 2:**  
     ```
     python Task2.py
     ```

---

## **Requirements**
- Python 3.x  
- No external libraries required  

---

## **Contributing**
Feel free to modify or improve these scripts. Contributions are welcome!  

---

## **License**
This project is open-source and free to use.


