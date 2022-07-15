from __future__ import unicode_literals, print_function
import re


def main():
    with open("show_version.txt") as f:
        lines = f.readlines()

    (version, serial_number, config_register) = [ "", "", ""]
    for line in lines:
        found_version = re.match('Cisco IOS.+Version (.+),', line)
        if found_version:
            version = found_version.group(1)
            continue
        found_reg = re.match('Configuration register is (.+)', line)
        if found_reg:
            config_register = found_reg.group(1)
            continue
        found_serial = re.match('Processor board ID (.+)', line)
        if found_serial:
            serial_number = found_serial.group(1)
            continue


    print("OS Version: {}".format(version))
    print("Serial Number: {}".format(serial_number))
    print("Config Register: {}".format(config_register))

# Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.4(2)T1, RELEASE SOFTWARE (fc3)
# Processor board ID FTX0000038X
# Configuration register is 0x2102

if __name__ == '__main__':
    main()