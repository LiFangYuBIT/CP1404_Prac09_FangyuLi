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
            new_name = get_fixed_filename(filename)
            print("Renaming {} to {}".format(filename, new_name))

            full_name = os.path.join(name, filename)
            new_name = os.path.join(name, new_name)
            os.rename(full_name, new_name)


def get_fixed_filename(filename):
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    return new_name


main()
# demo_walk()
