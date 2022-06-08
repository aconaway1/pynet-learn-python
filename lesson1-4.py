# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import re

def main():
    show_version = "*0        CISCO881-SEC-K9       FTX0000038X    "
    show_version = show_version.strip()

    dummy, model, serial = show_version.split()

    if re.search("cisco", model, re.IGNORECASE):
        print("This is a Cisco device.")
    if re.search("881", model, re.IGNORECASE):
        print("This is a model 881.")
    print("{:^15}{:^15}".format("Model", "Serial"))
    print("{:^15}{:^15}".format(model, serial))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()