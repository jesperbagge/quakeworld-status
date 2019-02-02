import socket


class QuakeWorldServer:
    def __init__(self, address, port=27500):
        self.address = address
        self.port = port

        self.STATUS = '\xff\xff\xff\xffstatus\x00'
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP message

    def __repr__(self):
        return 'QakeWorld server at {}'.format(self.address)

    def get_status(self):

        self.socket.sendto(bytes(self.STATUS, 'latin1'), (self.address, self.port))
        response = self.socket.recv(4096).decode('latin1').split('\n')

        info = response[0].split('\\')[1:]
        server = dict(zip(info[0::2], info[1::2]))

        players = [i for i in response[1:] if '\x00' not in i]

        return server, players
