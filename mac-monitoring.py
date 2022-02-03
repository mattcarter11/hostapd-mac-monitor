#!/usr/bin/env python3

import json
import time
import subprocess
import telegram_send

MAC_MONITORING_PATH = '/etc/hostapd/mac-monitoring.json'
STA = 'wlan0'


def get_connections(sta, monitoring):
    """ Returns MACs is sta that are being monitored """
    list_sta = subprocess.check_output(
        ["sudo", "hostapd_cli", "-i"+sta, "list_sta"]).decode('utf-8').splitlines()
    return [line for line in list_sta if line in monitoring]


def send(connections, disconnections):
    msg = f"<b>CONNECTED</b>\n{', '.join(connections)}\n\n<b>DISSCONECTED</b>\n{', '.join(disconnections)}"
    telegram_send.send(messages=[msg], parse_mode='html')


if __name__ == '__main__':
    with open(MAC_MONITORING_PATH, 'r') as file:
        monitoring = json.load(file)
    prev_connected = get_connections(STA, monitoring)
    while True:
        connected = get_connections(STA, monitoring)
        # List new connections
        connections = [mac for mac in connected if mac not in prev_connected]
        # List new disconnections
        disconnections = [
            p_mac for p_mac in prev_connected if p_mac not in connected]
        prev_connected = connected  # Save connectins for next iteration
        if connections != [] or disconnections != []:
            send(connections, disconnections)
        time.sleep(5)
