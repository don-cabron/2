# 2
## Homework 2 | Flask app | Ansible | 22.09.2021

## _This little app returns an emoji of animal_

## Environment

### VirtualBox:
- Install virtualbox. Instruction you can find [here][vbox].

- ISO of Debian 10.10 you can download [here][deb_iso].

- Then you need configure NAT or bridge between host and guest OS.

   > Note: In my case, I had to set NAT and bridge in the same time to get connection in local network and Internet.

- Find out IP of guest OS. 
   
   ```sh 
   ip addr
   ```
   Add IP you've found out to /etc/hosts of HOST MACHINE.
   ```sh
   sudo echo '192.168.100.x  myvm' >> /etc/hosts
   ```
   Try to ping guest OS.
   ```sh
   ping myvm
   ```

### SSH:
- Install openssh-client and openssh-server to host and guest OS.
   
   ```sh
   sudo apt install openssh-client openssh-server
   ```

- Generate keys and copy public key to guest OS.

   ```sh
   ssh-keygen
   ```

- Make sure .ssh/authorized_keys have chmod 600

- Try to connect to virtual machine.

   ```sh
   ssh root@myvm
   ```

> Note: These materials ([installation][ssh_installation], [problems][ssh_problems]) will help you if you have any problems. 

---

## Ansible
Install ansible to host machine.

```sh
sudo apt install ansible
```

Add guest OS to ansible's host file.

```sh
sudo echo 'myvm ansible_ssh_host=192.168.100.x ansible_ssh_user=root' >> /etc/ansible/hosts
```

Try to ping virtual machine.

```sh
ansible -m ping all
```

My result looks like this:

```sh
myvm | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python"
    },
    "changed": false,
    "ping": "pong"
}
```

Start playbook.

```sh
ansible-playbook playbook.yml -i /etc/ansible/hosts
```

Make request to app.

```sh
curl -X POST -d'{"animal":"cow", "sound":"moooo", "count":2}' http://myvm
```

Result:

```sh
🐄 says moooo
🐄 says moooo
Made with ❤ by @don_cabron
```








[vbox]: <https://www.virtualbox.org/wiki/Linux_Downloads>
[deb_iso]: <https://www.debian.org/releases/buster/debian-installer/>
[ssh_installation]: <https://help.ubuntu.ru/wiki/%D1%80%D1%83%D0%BA%D0%BE%D0%B2%D0%BE%D0%B4%D1%81%D1%82%D0%B2%D0%BE_%D0%BF%D0%BE_ubuntu_server/%D1%83%D0%B4%D0%B0%D0%BB%D0%B5%D0%BD%D0%BD%D0%BE%D0%B5_%D0%B0%D0%B4%D0%BC%D0%B8%D0%BD%D0%B8%D1%81%D1%82%D1%80%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5/openssh_server>
[ssh_problems]: <https://wiki.merionet.ru/servernye-resheniya/65/kak-nastroit-ssh-vxod-bez-parolya/>
