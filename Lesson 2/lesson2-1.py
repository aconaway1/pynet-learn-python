# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import re

def main():

    infile_name = "show_version.txt"
    f = open(infile_name)
    contents = f.read()
    print(contents)
    print("TYPE: {}".format(type(contents)))
    f.close()

    f = open(infile_name)
    lines = f.readlines()
    print(lines)
    print("TYPE: {}".format(type(lines)))
    f.close()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()