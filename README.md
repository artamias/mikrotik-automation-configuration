# MikroTik Network Automation with Python

This project shows how to automate basic MikroTik router configuration using Python.  
Instead of configuring the router manually through CLI or Winbox, this script connects via SSH and pushes the configuration automatically.

The automation is built using Python and Netmiko.

---

## ⚠️ Note (Initial Router Setup)

Before running the automation script, make sure the router can be accessed via SSH.

A new MikroTik router usually has **no password and no proper management IP**, so you need to configure it manually first.

Login to the router using **Winbox, WebFig, or terminal**, then set a password and management IP.

---

## IP Addressing Table

| Interface  | IP Address     | Port   |
|------------|----------------|--------|
| bridge-WAN | 192.168.65.131 | ether1 |
| bridge-LAN | 172.16.1.1     | ether2 |


## Project Goal

The goal of this project is to simplify the initial configuration process of a MikroTik router.

With Python script, the router will automatically:

- Create WAN bridge
- Create LAN bridge
- Add interfaces to the bridges
- Configure DHCP Client for WAN
- Enable NAT for internet access
- Configure DNS server
- Set LAN IP address
- Create DHCP Server for LAN clients

---

## Technologies Used

- Python
- Netmiko
- MikroTik RouterOS
- SSH

Python library used:

- netmiko

