# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 16:41:37 2016

@author: Fatih
"""

import socket 
s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
print(s)

server = 'pythonprogramming.net'
port = 80

server_ip = socket.gethostbyname(server)
print(server_ip)

request = "GET / HTTP/1.1\nHost: "+server+"\n\n"

s.connect((server, port))
s.send(request.encode())
result = s.recv(4096) ##buffer

print(result)

