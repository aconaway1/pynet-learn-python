from __future__ import unicode_literals, print_function
import re


def main():

    infile = open("show_arp.txt")
    default_info = []
    arista_info = []

    while infile:
        line = infile.readline()
        line.strip()
        arp_ip = ""
        arp_mac = ""
        if re.search("^Internet", line):
            arp_line = line.split()
            arp_ip = arp_line[1]
            arp_mac = arp_line[3]
        if re.search("10.220.88.1", line):
            default_info = (arp_ip, arp_mac)

        if re.search("10.220.88.30", line):
            arista_info = (arp_ip, arp_mac)

        if len(default_info) > 0 and len(arista_info) > 0:
            break

    infile.close()
    print("Default gateway IP/Mac is {} {}.".format(default_info[0], default_info[1]))
    print("Arista3 IP/Mac is {} {}.".format(arista_info[0], arista_info[1]))

if __name__ == '__main__':
    main()