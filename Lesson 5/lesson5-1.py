def ssh_conn(ipaddr, username, password):
    print("New SSH conn to {} using {}/{}.".format(ipaddr,username,password))

def main():
    ssh_conn('1.1.1.1', 'user1', 'pass1')
    ssh_conn(ipaddr='2.2.2.2', password='pass2', username='user2')
    ssh_conn('3.3.3.3', password='pass3', username='user3')

if __name__ == "__main__":
    main()