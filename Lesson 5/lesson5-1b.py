def ssh_conn(ipaddr, username, password, device_type="cisco_ios"):
    print("New SSH conn to {} at {} using {}/{}.".format(device_type,ipaddr,username,password))

def main():

    conn_dict = {
        'ipaddr': '10.1.1.1',
        'username': 'user9',
        'password': 'pass9',
        'device_type': 'fortios'
    }
    ssh_conn('1.1.1.1', 'user1', 'pass1')
    ssh_conn(ipaddr='2.2.2.2', password='pass2', username='user2', device_type='junos')
    ssh_conn('3.3.3.3', password='pass3', username='user3')
    ssh_conn(**conn_dict)

if __name__ == "__main__":
    main()