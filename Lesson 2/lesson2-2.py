# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import re

def main():

    my_addrs = []

    my_addrs.append("192.168.0.1")
    my_addrs.extend(['172.16.31.230', '10.1.1.33'])
    my_addrs += ['172.31.16.99', '10.255.255.2']

    print(my_addrs)
    print(my_addrs[0])
    print(my_addrs[-1])

    print(my_addrs.pop())
    print(my_addrs.pop(0))

    print(my_addrs)

    my_addrs[0] = '2.2.2.2'
    print(my_addrs)

if __name__ == '__main__':
    main()