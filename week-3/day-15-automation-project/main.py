# Day 15 — Python Automation Project
# File Organiser
#
# This automation scans an input folder and organises files
# into subfolders based on their file extensions.

import os
import shutil


# Configuration
INPUT_PATH = "data/"
OUTPUT_PATH = "data/output/"


def get_category(extension):
    """Return the folder category for a file extension."""

    extension = extension.lower()

    categories = {
        ".jpg": "images",
        ".jpeg": "images",
        ".png": "images",
        ".gif": "images",
        ".pdf": "documents",
        ".doc": "documents",
        ".docx": "documents",
        ".txt": "documents",
        ".mp3": "audio",
        ".wav": "audio",
        ".mp4": "videos",
        ".avi": "videos",
        ".mkv": "videos",
    }

    return categories.get(extension, "other")


def organise_files(input_path, output_path):
    """Scan the input folder and move files into organised folders."""

    # Edge case: input folder does not exist.
    if not os.path.isdir(input_path):
        print(f"Error: Input folder '{input_path}' was not found.")
        return

        files = os.listdir(input_path)

    # Ignore the output folder and Git placeholder when checking for input files.
    input_files = [
        filename
        for filename in files
        if filename != ".gitkeep"
        and os.path.isfile(os.path.join(input_path, filename))
    ]

    # Edge case: input folder contains no files to organise.
    if not input_files:
        print("The input folder is empty.")
        return

    os.makedirs(output_path, exist_ok=True)

    moved_count = 0

    for filename in files:
        source_path = os.path.join(input_path, filename)

        # Ignore directories.
        if not os.path.isfile(source_path):
            continue

        # Keep Git's placeholder file in the input folder.
        if filename == ".gitkeep":
            continue

        name, extension = os.path.splitext(filename)

        # Files without an extension go into "other".
        category = get_category(extension)

        category_path = os.path.join(output_path, category)
        os.makedirs(category_path, exist_ok=True)

        destination_path = os.path.join(category_path, filename)

        try:
            shutil.move(source_path, destination_path)
            print(f"Moved: {filename} -> {category}/")
            moved_count += 1

        except shutil.Error as error:
            print(f"Could not move {filename}: {error}")

        except OSError as error:
            print(f"File system error for {filename}: {error}")

    print(f"\nOrganisation complete. {moved_count} file(s) moved.")


def main():
    """Run the file organisation automation."""

    print("========================================")
    print("       DAY 15 - FILE ORGANISER")
    print("========================================")

    print(f"Input folder: {INPUT_PATH}")
    print(f"Output folder: {OUTPUT_PATH}\n")

    organise_files(INPUT_PATH, OUTPUT_PATH)


if __name__ == "__main__":
    main()
