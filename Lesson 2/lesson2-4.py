

def main():
    infile_name = "show_arp.txt"

    f = open(infile_name)
    lines = f.readlines()

    fe4_entries = lines[5]
    fe4_fields = fe4_entries.split()
    ip_addr = fe4_fields[1]
    int_name = fe4_fields[5]
    addr_tuple = (ip_addr, int_name)
    print(addr_tuple)


if __name__ == '__main__':
    main()
