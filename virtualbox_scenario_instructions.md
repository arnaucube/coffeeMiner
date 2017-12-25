### Instructions to setup VirtualBox scenario


In each machine, remember to setup the dns server, for example, in /etc/resolv.conf:

```
nameserver 8.8.8.8
```

### Victim
- network adapter:
    - Host-only Adapter
- /etc/network/interfaces:

```
auto lo
iface lo inet loopback

auto eth0
iface eth0 inet static
    address 10.0.2.20
    netmask 255.255.255.0
    gateway 10.0.2.15
```

### Attacker
- network adapter:
    - Host-only Adapter
- /etc/network/interfaces:

```
auto lo
iface lo inet loopback

auto eth0
iface eth0 inet static
    address 10.0.2.10
    netmask 255.255.255.0
    gateway 10.0.2.15
```


### Gateway
- network adapter:
    - Bridged Adapter
    - Host-only Adapter
- /etc/network/interfaces:

```
auto lo
iface lo inet loopback

auto eth0
iface eth0 inet dhcp

auto eth1
iface eth1 inet static
    address 10.0.2.15
    netmask 255.255.255.0
```

Clean IPTABLES:

```
iptables --flush
iptables --table nat --flush
```

Configure the Gateway machine as a router:

```
echo 1 > /proc/sys/net/ipv4/ip_forward

iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE

iptables -A FORWARD -i eth0 -o eth1 -j ACCEPT
iptables -A FORWARD -i eth1 -o eth0 -j ACCEPT
```
