import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
print("connecting on localhost port 10000")

while True:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(server_address)
        message=input('Message: ')
        if message=='quit':
            break
        sock.sendall(message.encode('utf-8'))
    except:
        break
sock.close()