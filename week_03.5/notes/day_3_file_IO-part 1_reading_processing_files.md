# Day 3: File I/O - Part 1: Reading and Processing Files - Study Material & Notes

## Introduction to File I/O

Welcome to Week 3.5, Day 3! Today, we're starting our exploration of **File Input/Output (I/O)** in Python. File I/O is a fundamental skill in programming that allows your programs to interact with files on your computer's file system.

**What is File I/O?**

- **Input (I):** Reading data _from_ a file into your program's memory. Think of it as your program "inputting" data from an external source (the file).
- **Output (O):** Writing data _from_ your program's memory _to_ a file. This is your program "outputting" data to be stored persistently in a file.

**Why is File I/O Important?**

File I/O is essential for many programming tasks, including:

- **Data Persistence:** Files are used to store data persistently, meaning the data remains even after your program ends. This is how you save information that needs to be used later (e.g., user settings, game save files, documents, databases).
- **Processing External Data:** Many programs need to work with data stored in external files, such as:
  - **Configuration Files:** Store settings and preferences for your application.
  - **Data Files:** Read data from text files, CSV files, JSON files, etc., for analysis, processing, or display.
  - **Log Files:** Write program events, errors, and debugging information to log files for monitoring and troubleshooting.
- **Interacting with Other Systems:** File I/O allows your programs to exchange data with other programs or systems by reading from and writing to files that are shared between them.

**Overview of File Operations:**

In general, working with files in programming involves these main steps:

1.  **Opening a File:** You need to "open" a file to establish a connection to it before you can read from it or write to it. This is like opening a door to access a room.
2.  **Performing Operations (Read or Write):** Once the file is open, you can perform operations:
    - **Reading:** Retrieve data from the file into your program.
    - **Writing:** Send data from your program to be stored in the file.
3.  **Closing the File:** After you are finished with the file, it's important to "close" it. This releases system resources and ensures that any pending write operations are completed and saved to the file. It's like closing the door after you leave the room.

Today, we will focus on **reading from files**. We'll cover writing to files tomorrow.

## File Paths: Navigating the File System

To work with a file, your program needs to know _where_ to find it on your computer's file system. This is done using **file paths**.

A **file path** is a string that specifies the location of a file or directory in a file system. There are two main types of file paths:

### 2.1. Absolute File Paths

- An **absolute file path** provides the _complete_ and _unambiguous_ location of a file, starting from the **root directory** of the file system.
- It always points to the same location, regardless of the current working directory of your program.

**Examples of Absolute File Paths:**

- **Linux/macOS:**

  - `/home/user/documents/my_report.txt`
  - `/usr/local/bin/python3`
  - `/var/log/system.log`
  - `/Users/username/Pictures/vacation_photo.jpg` (macOS example)

  In Linux and macOS, the root directory is represented by a single forward slash `/`.

- **Windows:**

  - `C:\Users\User\Documents\my_document.docx`
  - `D:\Projects\python_scripts\main.py`
  - `C:\Program Files\Mozilla Firefox\firefox.exe`

  In Windows, drive letters (like `C:`, `D:`) represent the root of each drive, and backslashes `\` are used as directory separators.

**Key Characteristics of Absolute Paths:**

- Start with the root directory indicator (`/` on Linux/macOS, drive letter like `C:\` on Windows).
- Provide the full path from the root to the file or directory.
- Are unambiguous and always point to the same location.

### 2.2. Relative File Paths

- A **relative file path** specifies the location of a file _relative_ to the **current working directory** of your program.
- The current working directory is the directory in which your Python script is being executed.

**Examples of Relative File Paths:**

Let's say your Python script is located in: `/home/user/projects/my_script/` (Linux/macOS) or `C:\Projects\my_script\` (Windows), and this is your current working directory.

- `data/input.txt` : This refers to a file named `input.txt` located in a subdirectory named `data` _within_ the current working directory.
- `report.csv` : This refers to a file named `report.csv` located in the _same_ directory as your script (the current working directory).
- `../logs/output.log` : `..` means "go up one directory level" (to the parent directory). So, this path refers to a file `output.log` located in a directory named `logs` that is in the _parent_ directory of the current working directory.
- `images/thumbnails/small_icon.png` : This refers to a file located in a nested directory structure: `images` subdirectory, then `thumbnails` subdirectory, and finally the file `small_icon.png`, all starting from the current working directory.

**Key Characteristics of Relative Paths:**

- Do _not_ start with a root directory indicator.
- Their meaning depends on the current working directory. If you change the working directory, the same relative path might refer to a different file or location.
- Are often shorter and more convenient when working with files within the same project directory structure.
- Make projects more portable because they don't rely on specific absolute paths that might be different on different computers.

**Current Working Directory:**

- When you run a Python script, it runs in a specific **current working directory**. By default, this is often the directory where you executed the script from the command line, or the directory of the script file itself, depending on how you run it.
- You can determine the current working directory in Python using the `os` module:

  ```python
  import os
  current_dir = os.getcwd() # Get current working directory
  print("Current Working Directory:", current_dir)
  ```

**Choosing Between Absolute and Relative Paths:**

- **Relative paths are generally preferred** for files that are part of your project and are located within the project's directory structure. This makes your project more portable and easier to share or move to different systems because the paths are relative to the project's base directory, not to specific absolute locations on a particular machine.
- **Absolute paths might be necessary** when you need to refer to files that are located outside of your project's directory structure, especially system-wide files (like log files in `/var/log` or program executables in `/usr/bin`). However, using absolute paths can make your code less portable and more dependent on the specific file system layout of a particular machine.

**Example Demonstration:**

Let's say you have a project directory like this:

```
my_project/
├── script.py
├── data/
│   └── input_data.txt
└── logs/
    └── output.log
```

If `script.py` is your current working directory (or if you run `script.py` from within `my_project/`), then:

- **Relative path to `input_data.txt`:** `data/input_data.txt`
- **Relative path to `output.log`:** `../logs/output.log`
- **Absolute path to `script.py` (example on Linux):** `/home/user/my_project/script.py` (This will vary depending on your actual user and project directory).

## 3. Opening Files for Reading: `open()` Function and Read Modes

To work with a file in Python, the first step is to **open** it using the built-in `open()` function.

**`open()` Function Syntax:**

```python
file_object = open(filename, mode, encoding=None)
```

- **`filename` (required):** A string representing the path to the file you want to open. This can be either an absolute or a relative file path.
- **`mode` (optional, default is `'r'`):** A string specifying the _mode_ in which you want to open the file. The mode determines what operations you can perform on the file (read, write, append, etc.) and how the file is handled.
- **`encoding` (optional):** A string specifying the character encoding to use when working with text files. This is important for handling different character sets correctly (e.g., UTF-8, ASCII, Latin-1). If you don't specify encoding for text files, Python uses a default encoding which might not always be correct for all files, especially those created on different systems or in different languages.

**Read Modes for `open()` (Focus for Day 3):**

For today, we'll focus on **read modes**, which are used for opening files to read data from them.

| Mode String | Description                                                                     | File Type |
| :---------- | :------------------------------------------------------------------------------ | :-------- |
| `'r'`       | **Read mode (text mode, default):** Opens a text file for reading.              | Text      |
| `'rt'`      | **Read text mode:** Explicitly specifies text mode for reading (same as `'r'`). | Text      |
| `'rb'`      | **Read binary mode:** Opens a binary file for reading.                          | Binary    |

**Explanation of Read Modes:**

- **`'r'` or `'rt'` (Read Text Mode):**

  - This is the **default mode** if you don't specify any mode in `open()`.
  - Opens a file for reading **text data**. Text files are files that contain human-readable characters (like letters, numbers, symbols, etc.), organized into lines.
  - Data read from the file will be returned as **strings**.
  - You should typically use this mode for `.txt`, `.csv`, `.json`, `.html`, `.py`, and other text-based files.
  - When using text mode, you should often specify the `encoding` argument (e.g., `encoding='utf-8'`) to ensure that characters are decoded correctly, especially for files that might contain characters outside of basic ASCII.

- **`'rb'` (Read Binary Mode):**
  - Opens a file for reading **binary data**. Binary files are files that are not primarily intended to be read as text. They contain raw bytes that represent data in a specific format (e.g., images, audio files, video files, executable files, compressed files).
  - Data read from the file in binary mode will be returned as **bytes objects** (not strings). Bytes objects are sequences of raw byte values (integers from 0 to 255).
  - You should use binary mode for files like `.jpg`, `.png`, `.mp3`, `.zip`, `.exe`, `.pdf`, etc.
  - **Do not use the `encoding` argument when opening files in binary mode**, as encodings are relevant to text files, not raw binary data.

**Specifying Encoding for Text Files:**

- **Character Encoding:** Text files store characters using a specific **character encoding**. Common encodings include:

  - **UTF-8:** A widely used encoding that can represent characters from almost all languages. It's a good default choice for text files in modern systems.
  - **ASCII:** A basic encoding for English characters and some symbols. Limited in its character set.
  - **Latin-1 (ISO-8859-1):** Another encoding that supports many Western European languages.
  - **Other encodings:** `utf-16`, `gbk`, `shift-jis`, etc., for specific languages or systems.

- **Importance of `encoding` Argument:** If you don't specify the correct `encoding` when opening a text file, Python might use a default encoding that is different from the encoding the file was actually saved in. This can lead to **`UnicodeDecodeError`** exceptions when you try to read the file, or you might see garbled or incorrect characters in your text.

- **Best Practice:** **Always specify `encoding='utf-8'` when opening text files for reading and writing** unless you have a specific reason to use a different encoding (and you know what encoding the file is in). UTF-8 is a very versatile and widely compatible encoding.

**Example: Opening a Text File in Read Mode**

```python
try:
    file = open("my_document.txt", 'r', encoding='utf-8') # Open in read text mode with UTF-8 encoding
    # ... perform read operations on the file ...
except FileNotFoundError:
    print("Error: File not found!")
except UnicodeDecodeError:
    print("Error: Could not decode file with UTF-8 encoding.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```

This example opens the file "my_document.txt" in read text mode (`'r'`) and specifies UTF-8 encoding. It also includes basic exception handling for `FileNotFoundError` (if the file doesn't exist) and `UnicodeDecodeError` (if there's an encoding problem).

## 4. Reading File Content: Methods and Iteration

Once you have opened a file in read mode (using `open()`), you can use various methods to read its content:

### 4.1. `read()` Method

- **Purpose:** The `read()` method reads the **entire content** of the file from the current position to the end and returns it as a single string (if opened in text mode) or bytes object (if opened in binary mode).

- **Syntax:**

  ```python
  file_content = file.read()
  ```

- **Example (Reading entire text file):**

  ```python
  try:
      file = open("my_poem.txt", 'r', encoding='utf-8')
      poem_text = file.read() # Read entire content into a single string
      print("--- File Content ---")
      print(poem_text)
      print("--- End of File Content ---")
  finally:
      file.close() # Ensure file is closed in finally block
  ```

- **Use Cases:**

  - When you need to process the entire file content as a whole (e.g., for simple text files, configuration files, small data files).
  - When you are sure that the file is not excessively large and can fit comfortably in memory.

- **Limitations:**
  - **Memory Usage:** If you use `read()` on a very large file (e.g., gigabytes in size), it will load the entire file content into memory at once, which can consume a lot of RAM and potentially cause memory issues or slow down your program.
  - **Not Suitable for Line-by-Line Processing:** If you need to process a file line by line, `read()` is not the most efficient method.

### 4.2. `readline()` Method

- **Purpose:** The `readline()` method reads a **single line** from the file, starting from the current position. It returns the line as a string (or bytes object in binary mode), **including the newline character `\n` at the end of the line (if present)**. If you call `readline()` again, it reads the next line, and so on. When you reach the end of the file, `readline()` returns an empty string `''`.

- **Syntax:**

  ```python
  line = file.readline()
  ```

- **Example (Reading file line by line using `readline()`):**

  ```python
  try:
      file = open("log_file.txt", 'r', encoding='utf-8')
      line = file.readline() # Read the first line
      while line: # Loop as long as readline() returns a non-empty string (i.e., not end of file)
          print("Line:", line.strip()) # Print line, removing leading/trailing whitespace (including newline)
          line = file.readline() # Read the next line
  finally:
      file.close()
  ```

  **Explanation:**

  - We use a `while` loop to repeatedly call `file.readline()`.
  - `line = file.readline()` reads a line and assigns it to the `line` variable.
  - The loop continues as long as `line` is not an empty string (meaning `readline()` successfully read a line). When `readline()` returns an empty string, it means we've reached the end of the file, and the loop terminates.
  - `line.strip()` is used to remove leading/trailing whitespace from the line, including the newline character `\n` that `readline()` includes.

- **Use Cases:**
  - Processing files line by line.
  - Memory-efficient reading of large files because it reads only one line at a time.
  - Parsing structured text files where each line represents a record or data entry.

### 4.3. `readlines()` Method

- **Purpose:** The `readlines()` method reads **all lines** from the file and returns them as a **list of strings** (or list of bytes objects in binary mode). Each string in the list represents a line, and it includes the newline character `\n` at the end of each line (except for the last line if it doesn't end with a newline).

- **Syntax:**

  ```python
  lines_list = file.readlines()
  ```

- **Example (Reading all lines into a list):**

  ```python
  try:
      file = open("data_lines.txt", 'r', encoding='utf-8')
      all_lines = file.readlines() # Read all lines into a list
      print("--- Lines in File ---")
      for line in all_lines:
          print("Line:", line.strip()) # Print each line, stripping whitespace
      print("--- End of Lines ---")
      print(f"Total lines read: {len(all_lines)}") # Get number of lines
  finally:
      file.close()
  ```

- **Use Cases:**

  - When you need to access all lines of a file as a list.
  - When you want to perform operations on the list of lines (e.g., filtering, sorting, indexing).
  - Suitable for files that are not excessively large, as it loads all lines into memory at once as a list.

- **Memory Considerations:** Like `read()`, `readlines()` can consume more memory for very large files because it reads all lines into a list in memory. For very large files, iterating over the file object (next method) is generally more memory-efficient.

### 4.4. Iterating Over a File Object (Efficient Line-by-Line Reading)

- **Purpose:** You can directly **iterate over a file object** in a `for` loop. When you do this, Python automatically reads the file **line by line** in a very memory-efficient way. This is often the **most recommended and efficient way** to read large text files line by line in Python.

- **Syntax:**

  ```python
  try:
      file = open("very_large_file.txt", 'r', encoding='utf-8')
      for line in file: # Iterate over the file object directly
          # Process each line here
          print("Line:", line.strip())
  finally:
      file.close()
  ```

- **Explanation:**

  - The `for line in file:` loop implicitly reads the file line by line. In each iteration, the `line` variable will contain the next line from the file (as a string, including the newline character).
  - This method is very memory-efficient because it reads and processes one line at a time, without loading the entire file into memory.

- **Use Cases:**
  - **Most efficient way to read large text files line by line.**
  - Processing log files, large data files, or any text file where you need to work with the content line by line.
  - When memory efficiency is important, especially for large files.

**Choosing the Right Reading Method:**

| Method        | Reads                                 | Returns                                | Memory Usage                       | Best Use Cases                                                                  |
| :------------ | :------------------------------------ | :------------------------------------- | :--------------------------------- | :------------------------------------------------------------------------------ |
| `read()`      | Entire file content                   | String (or bytes)                      | Potentially High (for large files) | Small files, when you need the entire content as a single string.               |
| `readline()`  | One line at a time                    | String (or bytes), empty string at EOF | Low (line by line)                 | Processing files line by line, memory efficiency for large files.               |
| `readlines()` | All lines at once                     | List of strings (or bytes)             | Potentially High (for large files) | When you need all lines as a list, files not too large.                         |
| Iteration     | Line by line (implicit in `for` loop) | String (or bytes) in each iteration    | Very Low (line by line)            | Most efficient for large text files, line-by-line processing, memory-sensitive. |

## 5. Closing Files: The `close()` Method

After you are done working with a file (reading or writing), it's **crucial to close it** using the `close()` method.

**Why Close Files?**

- **Release System Resources:** When you open a file, the operating system allocates resources to manage that file connection (file handles, memory buffers, etc.). If you don't close files properly, especially in long-running programs or when dealing with many files, you can exhaust system resources, leading to performance issues or errors.
- **Ensure Data is Written to Disk (for writing):** When you write data to a file, the data might be initially stored in memory buffers. Closing the file typically flushes these buffers and ensures that all data is physically written to the disk. If your program crashes or exits unexpectedly before closing a file you were writing to, some data might be lost or corrupted.
- **Prevent File Corruption and Sharing Issues:** Leaving files open unnecessarily can sometimes lead to file corruption or problems if other programs or processes try to access or modify the same file.

**The `close()` Method:**

- To close a file, you call the `close()` method on the file object:

  ```python
  file.close()
  ```

- **Example (Explicitly closing a file):**

  ```python
  file = open("my_data.txt", 'r', encoding='utf-8')
  try:
      content = file.read()
      print(content)
  finally: # Use finally to ensure file is closed even if errors occur
      file.close()
  ```

  **Explanation:**

  - We use a `finally` block to ensure that `file.close()` is always called, regardless of whether the `try` block executes successfully or if an exception occurs within it. This is a common pattern to guarantee file closure.

**Forgetting to Close Files (Common Mistake):**

- A common mistake, especially for beginners, is to forget to close files after using them. In many cases, Python might automatically close files when the file object is no longer referenced (garbage collection). However, relying on this automatic closure is **not good practice**. It's better to **explicitly close files** to ensure resource release and data integrity, especially in more complex programs or when dealing with file writing.

**Context Managers (`with open(...) as f:` - Preview for Day 4):**

- Tomorrow, we will learn about **context managers** and the `with open(...) as f:` statement. This is a more Pythonic and robust way to work with files because it **automatically handles file closing for you**, even if exceptions occur. Using `with open(...)` is generally the **recommended best practice** for file I/O in Python, as it simplifies file handling and reduces the risk of forgetting to close files.

**For today, it's important to understand the `close()` method and the importance of closing files explicitly, especially when you are not yet using context managers.**

## Summary of Day 3: File I/O - Part 1

Today, we've covered the fundamentals of File I/O in Python, focusing on reading files:

- **File I/O Importance:** Why file I/O is crucial for data persistence, external data, and program interaction.
- **File Paths:** Absolute vs. relative file paths and how to navigate the file system.
- **`open()` Function and Read Modes:** How to open files for reading using `open()` with modes `'r'`, `'rt'`, and `'rb'`, and the importance of `encoding` for text files.
- **Reading Methods:** `read()`, `readline()`, `readlines()`, and efficient iteration over file objects for line-by-line reading. Choosing the right method based on file size and processing needs.
- **Closing Files:** The `close()` method and why it's important to close files to release resources and ensure data integrity.

These are essential building blocks for working with files in Python. Tomorrow, we will continue with **File I/O - Part 2**, where we will learn about writing to files and explore context managers for more elegant and robust file handling!

## Exercises

**Exercise 1: File Statistics - Basic Reading**

1.  **Create a text file:** Create a new text file named `sample.txt` (or any name you like) and put some text content into it (a few lines of text, maybe some sentences or a short paragraph). Save it in the same directory as your Python script, or in a subdirectory if you prefer.
2.  **Write a Python script:** Write a Python script that does the following:
    - Asks the user to enter the filename (e.g., "sample.txt").
    - Opens the file in read text mode (`'r'`, with `encoding='utf-8'`).
    - Reads the entire content of the file using `read()`.
    - Prints the entire file content to the console.
    - Closes the file.
    - Include basic error handling (e.g., `try...except FileNotFoundError`) in case the user enters a filename that doesn't exist.

**Exercise 2: Line Count and Word Count**

1.  **Use the same `sample.txt` file** (or create a new one with more text if you like).
2.  **Write a Python script** that:
    - Asks the user for the filename.
    - Opens the file in read text mode.
    - Reads the file line by line using a `for` loop (iterating over the file object).
    - Counts the total number of lines in the file.
    - Counts the total number of words in the file (you can split each line into words using `line.split()`).
    - Prints the line count and word count to the console.
    - Closes the file.
    - Include error handling for `FileNotFoundError` and any other potential `IOError` that might occur during file reading.

**Exercise 3: Read First N Lines**

1.  **Use the `sample.txt` file** (or create a longer text file if you want to test with more lines).
2.  **Write a Python script** that:
    - Asks the user for the filename and the number of lines to read (let's say `n`).
    - Opens the file in read text mode.
    - Reads and prints only the **first `n` lines** of the file to the console. Use `readline()` or iteration to read line by line.
    - If the file has fewer than `n` lines, print all lines in the file.
    - Closes the file.
    - Handle `FileNotFoundError` and potential `IOError` exceptions.

**Self-Check Questions (Optional):**

- What is the difference between absolute and relative file paths? When is it better to use relative paths?
- Explain the purpose of the `open()` function in Python. What are the common read modes (`'r'`, `'rt'`, `'rb'`) and when would you use each?
- What is the `encoding` argument in `open()` and why is it important for text files? What is a common encoding to use?
- Describe the differences between `read()`, `readline()`, and `readlines()` methods for reading file content. When would you choose to use each method?
- Why is it important to close files after you are finished with them? What is the `close()` method used for?

## Daily Task

**Task: Display File Content with Line Numbers**

Write a Python script that:

1.  Asks the user for a filename.
2.  Opens the file in read text mode.
3.  Reads the file line by line (using iteration).
4.  For each line, print the **line number** followed by the line content (e.g., "Line 1: This is the first line."). Start line numbering from 1.
5.  Close the file.
6.  Include error handling for `FileNotFoundError`.

For example, if `sample.txt` contains:

```
First line of text.
Second line is here.
Third and last line.
```

The output of your script should be:

```
Line 1: First line of text.
Line 2: Second line is here.
Line 3: Third and last line.
```

---

## Solutions to Exercises and Daily Task

<details>
<summary><b>Solution for Exercise 1: File Statistics - Basic Reading</b></summary>

```python
filename = input("Enter filename: ")

try:
    file = open(filename, 'r', encoding='utf-8')
    file_content = file.read()
    print("--- File Content ---")
    print(file_content)
    print("--- End of File Content ---")
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    if 'file' in locals() and not file.closed: # Check if file was opened and not already closed
        file.close()
```

</details>

<details>
<summary><b>Solution for Exercise 2: Line Count and Word Count</b></summary>

```python
filename = input("Enter filename: ")
line_count = 0
word_count = 0

try:
    file = open(filename, 'r', encoding='utf-8')
    for line in file:
        line_count += 1
        words = line.split() # Split line into words (by whitespace)
        word_count += len(words)
    print(f"File: '{filename}'")
    print(f"Line Count: {line_count}")
    print(f"Word Count: {word_count}")
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
except IOError as e:
    print(f"I/O Error: {e}")
finally:
    if 'file' in locals() and not file.closed:
        file.close()
```

</details>

<details>
<summary><b>Solution for Exercise 3: Read First N Lines</b></summary>

```python
filename = input("Enter filename: ")
try:
    n_lines = int(input("Enter number of lines to read: "))
except ValueError:
    print("Invalid input for number of lines. Please enter an integer.")
    n_lines = 0 # Default to 0 if input is invalid

if n_lines > 0:
    try:
        file = open(filename, 'r', encoding='utf-8')
        line_number = 0
        for _ in range(n_lines): # Loop n times or until end of file
            line = file.readline()
            if not line: # End of file reached
                break
            line_number += 1
            print(f"Line {line_number}: {line.strip()}") # Print line with line number
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except IOError as e:
        print(f"I/O Error: {e}")
    finally:
        if 'file' in locals() and not file.closed:
            file.close()
else:
    print("Number of lines to read must be positive.")
```

</details>

<details>
<summary><b>Solution for Daily Task: Display File Content with Line Numbers</b></summary>

```python
filename = input("Enter filename: ")

try:
    file = open(filename, 'r', encoding='utf-8')
    line_number = 1
    for line in file:
        print(f"Line {line_number}: {line.strip()}") # Print line number and line content
        line_number += 1
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
except IOError as e:
    print(f"I/O Error: {e}")
finally:
    if 'file' in locals() and not file.closed:
        file.close()
```

</details>

---

**End of Day 3 Study Material & Notes**
