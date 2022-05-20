"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
# import shutil
import os


def main():
    """Demo os module functions."""

    # Change to desired directory
    os.chdir('Lyrics')

    for name, contents, filenames in os.walk('.'):

        for filename in filenames:

            new_name = get_fixed_filename(get_space(filename))
            print(f"Renaming {filename} to {new_name}")
            full_name = os.path.join(name, filename)
            new_name = os.path.join(name, new_name)
            os.rename(full_name, new_name)


def get_fixed_filename(filename):
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    return new_name


def get_space(filename):

    if ' ' in filename or "_" in filename:
        return filename
    else:
        for j in range(len(filename) - 1):
            if filename[j].islower() and filename[j + 1].isupper():
                filename = filename[:j + 1] + ' ' + filename[j + 1:]
        return filename


main()
