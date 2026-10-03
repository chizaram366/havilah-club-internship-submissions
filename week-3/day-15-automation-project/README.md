
# Day 15 — Python Automation Project

## What does this project do?

This project is a **File Organiser** built with Python. It automatically scans an input folder and moves files into organised subfolders based on their file extensions. This makes files easier to find and keeps the folder organised without manually sorting each file.

## Project Type

**File Organiser**

## Input → Process → Output

### Input

The program reads files from:

```text
data/
```

The sample input includes files with different extensions:

* `report.pdf`
* `photo.jpg`
* `song.mp3`
* `notes.txt`
* `video.mp4`
* `no_extension`

### Process

The program:

1. Checks whether the input folder exists.
2. Reads the files inside the input folder.
3. Identifies each file's extension.
4. Assigns the file to an appropriate category.
5. Creates the required output folder.
6. Moves each file into its category folder.
7. Reports how many files were successfully moved.

### Output

Organised files are placed inside:

```text
data/output/
```

The output categories are:

```text
audio/
documents/
images/
other/
videos/
```

For example:

```text
report.pdf  → documents/
photo.jpg   → images/
song.mp3    → audio/
video.mp4   → videos/
no_extension → other/
```

## Requirements

This project uses Python's standard library only.

No external packages are required.

The main modules used are:

* `os` — for working with folders and file paths.
* `shutil` — for moving files.

Python 3 is required.

## How to Run

Open PowerShell in the project folder:

```text
week-3/day-15-automation-project
```

Then run:

```bash
python main.py
```

The program will scan the `data/` folder and organise the files automatically.

## Example Output

```text
========================================
       DAY 15 - FILE ORGANISER
========================================
Input folder: data/
Output folder: data/output/

Moved: report.pdf -> documents/
Moved: photo.jpg -> images/
Moved: song.mp3 -> audio/
Moved: notes.txt -> documents/
Moved: no_extension -> other/
Moved: video.mp4 -> videos/

Organisation complete. 6 file(s) moved.
```

## Edge Cases Handled

The program handles several possible problems safely.

### 1. Missing input folder

If the `data/` folder does not exist, the program displays an error message instead of crashing:

```text
Error: Input folder 'data/' was not found.
```

### 2. Empty input folder

If the input folder contains no files to organise, the program reports:

```text
The input folder is empty.
```

### 3. Files without extensions

Files without an extension are placed into the `other/` folder.

Example:

```text
no_extension → other/
```

### 4. Unexpected file extensions

Files with extensions that are not in the predefined categories are also placed into the `other/` folder.

### 5. Directories inside the input folder

Directories are ignored because the program only processes files.

## Project Structure

```text
day-15-automation-project/
│
├── main.py
├── README.md
│
└── data/
    ├── .gitkeep
    │
    └── output/
        ├── audio/
        │   └── song.mp3
        ├── documents/
        │   ├── notes.txt
        │   └── report.pdf
        ├── images/
        │   └── photo.jpg
        ├── other/
        │   └── no_extension
        └── videos/
            └── video.mp4
```

## Functions

The program is divided into clearly named functions:

* `get_category()` — determines the category for a file extension.
* `organise_files()` — scans the folder and moves files.
* `main()` — starts the automation.

This structure keeps the code organised and makes each function responsible for a specific task.

## Testing

The automation was tested using normal sample files with different extensions.

The following edge cases were also tested:

* Missing input folder
* Empty input folder
* File without an extension

The program handled these cases without crashing.

## Expected Result

After running the program, files should be automatically organised into extension-based category folders under:

```text
data/output/
```

The automation reduces the need for manual file sorting and demonstrates practical Python file and folder automation.
