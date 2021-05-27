import hashlib
from datetime import datetime

class Block():
    def __init__(self,prevHash,data):
        self.prevHash  = prevHash
        self.data      = data
        self.timestamp = datetime.now()
        self.hash      = self.makeHash()
        self.nonce     = 0

    def makeHash(self):
        hash = hashlib.sha256((str(self.data) + str(self.prevHash) + str(self.timestamp) + str(self.nonce)).encode())
        return hash.hexdigest()

    def mineblock(self,difficulty):
        while(self.hash[:difficulty] == "0"*difficulty+'x'):
            self.hash += 1
            self.hash = self.makeHash()


