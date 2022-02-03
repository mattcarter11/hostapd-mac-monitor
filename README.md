# A brief explanation
This script provides way to setup a monitoring service of specific MACs for a Hostapd Wifi Access Point.

# Setup
1. Install python3

2. Install telegram-send for python3

3. Create your own telegram bot and configure [telegram-send](https://medium.com/@robertbracco1/how-to-write-a-telegram-bot-to-send-messages-with-python-bcdf45d0a580)

	⚠Important, since the script runs as root, set the configuration of telegram-send as root:

        $ sudo telegram-send --configure

4. Setup *hostapd* and enable *hostapd_cli* by adding to the config

        ctrl_interface=/var/run/hostapd
        ctrl_interface_group=0

5. Place the *mac-monitoring.py*, *mac-monitoring.json* in */etc/hostapd/*

6. Place the daemon file *mac-monitoring.service* at */etc/systemd/system/* and start the daemon

        $ sudo systemctl daemon-reload
        $ sudo systemctl enable --now mac-monitoring
        $ sudo systemctl restart mac-monitoring

7. Configure the MACs you want to monitor

# Configure the MACs to monitor
1. Set your MAC monitoring filter with the file *ac-monitoring.json*. The format is:

```
["mac0", …, "macN"]
```

2. Restart the daemon

```bash
$ sudo systemctl restart mac-monitoring
```	
		
# *mac-monitoring.json*
## format
	
```
["mac0", …, "macN"]
```

## example
```json
["48:01:C5:76:14:53", "87:0F:32:45:01:64"]
```
