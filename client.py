import socket


def checkData(data):
    return (data.endswith('[CR]')
            or data.endswith('CR')) \
           and data.count(' ') == 3 \
           and data.count(':') == 2 \
           and data.count('.') == 1


address_to_server = ('localhost', 9285)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(address_to_server)
# client.send(bytes('0005 U1 05:12:02.877 10[CR]', encoding='UTF-8'))
data = str(input("Enter the data in the form of BBBBxNNxHH:MM:SS.zhqxGGCR: "))
if checkData(data):
    client.send(bytes(data, encoding='UTF-8'))
else:
    client.send(bytes("Incorrect data", encoding='UTF-8'))
clientDataFromServer = client.recv(1024)
print(str(clientDataFromServer.decode("utf-8")))
