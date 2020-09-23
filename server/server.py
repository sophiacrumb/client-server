import socket

localIP = "127.0.0.1"
localPort = 20002
buf_size = 1024

msgFromServer = "It's a server"
bytesToSend = str.encode(msgFromServer)

UPDServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UPDServerSocket.bind((localIP, localPort))

print("UDP Server is up")
while True:
    bytesAddressPair = UPDServerSocket.recvfrom(buf_size)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientMsg = "Message from Client:{}".format(message)
    clientIP = "Client IP Address:{}".format(address)
    print(clientMsg)
    print(clientIP)
    UPDServerSocket.sendto(bytesToSend, address)
