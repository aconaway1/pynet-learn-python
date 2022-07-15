from __future__ import unicode_literals, print_function
import re


def main():
    with open("show_ipv6_intf.txt") as f:
        lines = f.readlines()

    for line in lines:
        match = re.search(r'^\s+\d{1,4}:', line)
        if match:
            print(line.split()[0])

if __name__ == '__main__':
    main()