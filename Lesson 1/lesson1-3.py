# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    ip6_1 = "2001:db8:1234::1"
    IP6_2 = "2001:db8:1234::2"
    ip6_addr3 = "2001:db8:1234::3"

    print("Does the first var equal the second? {}".format(ip6_1 == IP6_2))
    print("Does the second var NOT equal the third? {}".format(IP6_2 != ip6_addr3))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()