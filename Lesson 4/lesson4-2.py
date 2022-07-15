from __future__ import unicode_literals, print_function



def main():
    houston_routers = ["192.168.1.1", "192.168.2.1", "172.31.254.254", "192.168.1.1", "192.168.2.3", "10.1.1.5", "10.1.1.6", "172.31.254.254", "10.1.1.1"]
    atlanta_routers = ["172.31.254.254", "10.1.1.1", "10.1.1.2", "10.1.1.3", "10.1.1.4", "10.1.1.5", "10.1.1.6", "10.1.1.7"]
    chicago_routers = ["172.31.254.254", "10.1.1.1", "10.1.1.2", "10.1.1.3", "10.1.1.6", "10.1.1.7", "192.168.2.3", "10.1.1.25", "10.1.1.6", "172.31.254.254", "10.1.1.1"]

    hou_set = set(houston_routers)
    atl_set = set(atlanta_routers)
    chi_set = set(chicago_routers)

    print("Duplicates between HOU and ATL")
    print(hou_set.intersection(atl_set))
    print("-" * 30)

    print("Duplicates among all sites")
    print(hou_set.intersection(atl_set).intersection((chi_set)))
    print("-" * 30)

    print("Unique address in CHI")
    print(chi_set.difference(atl_set.union(hou_set)))
    print("-" * 30)

if __name__ == '__main__':
    main()