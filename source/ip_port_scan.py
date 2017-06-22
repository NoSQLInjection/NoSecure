#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import socket
import time
import thread

socket.setdefaulttimeout(3)


def socket_port(ip, port,port_list):
    """
    输入IP和端口号，扫描判断端口是否开放
    """
    try:
        if port >= 65535:
            pass
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((ip, port))
        if result == 0:
            lock.acquire()
            port_list.append(port)
            lock.release()
        s.close()
    except:
        pass


def ip_scan(ip):
    """
    输入IP，扫描IP的0-65534端口情况
    """
    port_list = []
    try:
        start_time = time.time()
        for i in range(0, 65534):
            thread.start_new_thread(socket_port, (ip, int(i),port_list))
    except:
        pass
    return port_list