from netmiko import ConnectHandler

mikrotik_router = {
    'device_type': 'mikrotik_routeros', 
    'host': 'your-mikrotik-IP',
    'username': 'admin',
    'password': '#your-password-mikrotik',
}

ConnectHandler = ConnectHandler(**mikrotik_router)
command = [
    'interface bridge add name=bridge-WAN',
    'interface bridge port add interface=ether1 bridge=bridge-WAN',
    'interface bridge add name=bridge-LAN',
    'interface bridge port add interface=ether2 bridge=bridge-LAN',
    'ip dhcp-client set 0 interface=bridge-WAN disabled=no use-peer-dns=no',
    'ip firewall nat add chain=srcnat out-interface=bridge-WAN action=masquerade',
    'ip dns set servers=8.8.8.8,8.8.4.4 allow-remote-requests=yes',
    'ip address add address=172.16.1.1/24 interface=bridge-LAN',
    'ip pool add name=dhcp_pool_LAN ranges=172.16.1.2-172.16.1.254',
    'ip dhcp-server add name=dhcp_LAN interface=bridge-LAN address-pool=dhcp_pool_LAN disabled=no',
    'ip dhcp-server network add address=172.16.1.0/24 gateway=172.16.1.1 dns-server=8.8.8.8,8.8.4.4'
]
output = ConnectHandler.send_config_set(command)

print(output)
