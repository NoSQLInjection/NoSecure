#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import requests
import socket
from ip_port_scan import *


def server_query(url):
    r = requests.get(url)
    if 'server' in r.headers:
        server = r.headers['server']
    else:
        server='Nothing back:P'

    subdomain = url.split('://')[1]
    ip = socket.gethostbyname(subdomain)
    lock = thread.allocate_lock()
    port_list=ip_scan(ip)
    f = open(subdomain+'.txt','w')
    f.write("subdomain\n")
    f.write(subdomain)
    f.write("\nip\n")
    f.write(ip)
    f.write("\nserver\n")
    f.write(server)
    f.write("\nport_list\n")
    for port in port_list:
        f.write(port)
        f.write("\n")
    f.close()
server_query('https://www.baidu.com')
