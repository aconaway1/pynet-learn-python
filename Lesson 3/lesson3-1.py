from __future__ import unicode_literals, print_function
import re


def main():

    infile = open("show_vlan.txt")
    lines = infile.readlines()

    vlan_list = []

    for line in lines:
        line.strip()
        if re.search("^\d+\s+\w+", line):
            vlan_line = line.split()

            vlan_list.append((vlan_line[0], vlan_line[1]))

    print(vlan_list)


if __name__ == '__main__':
    main()