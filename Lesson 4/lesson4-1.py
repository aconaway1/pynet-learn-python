from __future__ import unicode_literals, print_function



def main():
    netdev_dict = {
        'ip_addr': "192.168.0.1",
        'vendor': "juniper",
        'username': "admin",
        'password': "adminpass",
    }

    bgp_fields = {
        'bgp_as': 100,
        'peer_as': 200,
        'peer_ip': "10.1.1.2",
    }

    if netdev_dict.get('vendor') == "cisco":
        netdev_dict['platform'] = "ios"
    if netdev_dict.get("vendor") == "juniper":
        netdev_dict['platform'] = "junos"

    netdev_dict.update(bgp_fields)

    for key, value in netdev_dict.items():
        print("{} -- {}".format(key, value))


if __name__ == '__main__':
    main()