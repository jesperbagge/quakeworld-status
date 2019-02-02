import socket


class QuakeWorldServer:
    def __init__(self, address, port=27500, timeout=10):
        self.address = address
        self.port = int(port)
        self.timeout = timeout

    def __repr__(self):
        return 'QuakeWorld server at {}'.format(self.address)

    def _get_status(self):

        msg = '\xff\xff\xff\xffstatus\x00'
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        s.settimeout(self.timeout)
        s.sendto(bytes(msg, 'latin1'), (self.address, self.port))
        response = s.recv(4096).decode('latin1').split('\n')

        info = response[0].split('\\')[1:]
        server = dict(zip(info[0::2], info[1::2]))

        players = [i for i in response[1:] if '\x00' not in i]

        return server, players

    def info(self):

        try:
            server, players = self._get_status()
            return server
        except:
            return 'Unable to reach server.'

    def players(self):

        try:
            server, players = self._get_status()
            return players
        except:
            return 'Unable to reach server.'
