import socket

UDP_IP = socket.gethostbyname("nickspi.student.umd.edu")
UDP_PORT = 42297

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
sock.bind((UDP_IP, UDP_PORT))
response = sock.recvfrom(1024)
print response
