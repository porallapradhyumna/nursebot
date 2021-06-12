
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 20:23:52 2021

@author: PRADHYUMNA
"""

import socket

HOST = '192.168.29.147'  # The server's hostname or IP address
PORT = 65432        # The port used by the server
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall(b'cap')
data = s.recv(1024).decode("utf-8") 
s.close()
print('Received' , repr(data))



