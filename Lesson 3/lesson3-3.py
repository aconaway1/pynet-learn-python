from __future__ import unicode_literals, print_function
import re


def main():

    infile = open("show_lldp_neighbor_details.txt")

    found_id = False
    found_name = False

    while infile:
        line = infile.readline()
        line.strip()
        if re.search("^Port id:", line):
            print(line.split(":")[1])
            found_id = True
        if re.search("^System Name:", line):
            print(line.split(":")[1])
            found_name = True
        if found_name and found_id:
            break


    infile.close()

if __name__ == '__main__':
    main()