from __future__ import unicode_literals, print_function
import os

WINDOWS = True

def main():
    base_cmd_linux = 'ping -c 2 '
    base_cmd_windows = 'ping -n 2 '
    base_cmd = base_cmd_windows if WINDOWS else base_cmd_linux

    base_address = "192.168.254."
    full_address_list = []
    for host in range(1, 255):
        full_address_list.append("{}{}".format(base_address, host))

    for index, value in enumerate(full_address_list):
        print("{} ---> {}".format(index, value))

    short_address_list = full_address_list[66:69]

    for address in short_address_list:
        os.system(base_cmd + address)


if __name__ == '__main__':
    main()