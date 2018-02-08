#!/usr/bin/python3

''' This program functions as a server by listening to a port
when it receives  a request at the port, it does something
this program could run anywhere, but I will be using it on a Rasp Pi
here is the reference I have used:
https://www.thoughtco.com/building-a-simple-web-server-2813571
'''

''' NOTE: I think this program would work if the client sends requests
in byte format instead of string format.
See this article for simple type conversions:
https://www.mkyong.com/python/python-3-convert-string-to-bytes/
...
I will explore alternate solution that works with strings.
Second option is to figure out how to use buffered stream instead of unbuffered
'''

import socket

host = ''
port = 53531

c = socket.socket()
# c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# c = socket.socket(socket.AF_INET, socket.SOCK_RAW)
c.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

c.bind((host, port))
c.listen(1)

while 1: 
    csock, caddr = c.accept() 
    cfile = csock.makefile('rwb', 0)
    line = cfile.readline().strip()
    line = b'You sent this: ' + line
    cfile.write(line)
    # cfile.write(b'You sent this: {}'.format(line))
    cfile.close() 
    csock.close()  
