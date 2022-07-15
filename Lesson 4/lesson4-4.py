from __future__ import unicode_literals, print_function
import re


def main():
    show_version = '''
    Cisco 881 (MPC8300) processor (revision 1.0) with 236544K/25600K bytes of memory.
    Processor board ID FTX0000038X

    5 FastEthernet interfaces
    1 Virtual Private Network (VPN) Module
    256K bytes of non-volatile configuration memory.
    126000K bytes of ATA CompactFlash (Read/Write)
    '''

    result = re.search('Cisco (?P<model>\d+)', show_version)
    model = result.group('model')

    result = re.search('with (?P<memory>\w+/\w+) bytes', show_version)
    memory = result.group('memory')

    print(model)
    print(memory)

if __name__ == '__main__':
    main()