

def main():
    f = open("show_ip_bgp_summ.txt")
    lines = f.readlines()
    first_line = lines[0].strip()
    last_line = lines[-1].strip()

    as_lines = first_line.split("local AS number ")
    as_number = as_lines[-1]

    peer_lines = last_line.split()
    peer_addr = peer_lines[0]

    print("AS: {}  Peer: {}".format(as_number, peer_addr))

if __name__ == '__main__':
    main()
