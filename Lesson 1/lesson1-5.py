# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import re

def main():
    col_width = 20
    col_format = "{:>" + str(col_width) + "} {:>" + str(col_width) + "}"

    mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
    mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
    mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"

    print(col_format.format("IP ADDR", "MAC ADDRESS"))
    print("-" * col_width, end=" ")
    print("-" * col_width)
    print(col_format.format(mac1.split()[1], mac1.split()[3]))
    print(col_format.format(mac2.split()[1], mac2.split()[3]))
    print(col_format.format(mac3.split()[1], mac3.split()[3]))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()