import socket

msgFromClient = "It's client using UDP"
bytesToSend = str.encode(msgFromClient)
serverAddress = ("127.0.0.1", 20002)
buf_size = 1024

UDPClientSocket = socket.socket(family=socket.AF_INET, type = socket.SOCK_DGRAM)
UDPClientSocket.sendto(bytesToSend, serverAddress)
msgFromServer = UDPClientSocket.recvfrom(buf_size)

msg = "Message from Server {}".format(msgFromServer[0])

print(msg)
