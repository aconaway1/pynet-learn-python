import random

def gen_addr(base_addr='10.10.10.', mask='/24'):
    return ("{}{}{}".format(base_addr,random.randint(1, 254),mask))


def main():
    print(gen_addr())
    print(gen_addr('192.168.1.'))
    print(gen_addr(base_addr='172.16.39.', mask='/22'))

if __name__ == "__main__":
    main()