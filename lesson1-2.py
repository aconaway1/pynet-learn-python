# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    headers = [
        "Octet1",
        "Octet2",
        "Octet3",
        "Octet4"
    ]

    ip_address = input("Please enter an IP address:")
    octets = ip_address.split('.')

    for header in headers:
        print("{:^15}".format(header), end="")
    print()
    print("-" * 60)
    print("{:^15}{:^15}{:^15}{:^15}".format(*octets))
    for octet in octets:
        print("{:^15}".format(bin(int(octet))), end="")
    print()
    for octet in octets:
        print("{:^15}".format(hex(int(octet))), end="")
    print()
    print("-" * 60)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()