import socket


def result(bb, nn, hh, ss, zhq, group, sender):
    f = open('log.txt', 'a', encoding='utf-8')
    log = str("Спортсмен, нагрудный номер " + bb + " прошел отсечку " + nn + " в " + hh + ":" +
              ss + ":" + zhq[0] + "." + zhq[1][0])
    f.write(str(sender) + " (" + str(group) + ")" + " " + log + '\n')
    f.close()
    return log


SERVER_ADDRESS = ('localhost', 9285)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(SERVER_ADDRESS)
server_socket.listen(10)
print('Server has started. ')

while True:
    connection, address = server_socket.accept()
    print("{address} has connected to the server".format(address=address))

    data = connection.recv(1024)
    if data:
        strData = str(data.decode('utf-8'))
        if strData == 'Incorrect data':
            connection.send(
                bytes('Unfortunately, server has received incorrect data, try again soon', encoding='utf-8'))
            connection.close()
            f = open('log.txt', 'a', encoding='utf-8')
            f.write(str(address) + ' sent incorrect data\n')
            f.close()
        else:
            dataList = strData.split(' ')
            dataTimeList = dataList[2].split(':')
            dataTimeSecondsList = dataTimeList[2].split('.')
            try:
                dataGroup = dataList[3][0:dataList[3].index('[CR]')]
            except ValueError:
                dataGroup = dataList[3][0:dataList[3].index('CR')]
            print(str("Received: " + strData))
            res = result(dataList[0], dataList[1], dataTimeList[0], dataTimeList[1], dataTimeSecondsList, dataGroup,
                         address)
            if dataGroup == '00':
                connection.send(bytes(res, encoding='utf-8'))

            connection.close()
