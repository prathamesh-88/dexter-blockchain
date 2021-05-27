from package.block import Block
import hashlib


class Blockchain():
    def __init__(self):
        self.blockchain = {};
        self.__genesisBlock = Block(hashlib.sha256("satoshi nakamoto".encode()).hexdigest(),{"hello":"hello"})
        self.blockchain[self.__genesisBlock.hash] = self.__genesisBlock
        self.__latest_block = self.__genesisBlock.hash
        self.difficulty     = 4
    
    def addBlock(self, data):
        newBlock = Block(self.__latest_block,data)
        newBlock.mineblock(self.difficulty)
        self.blockchain[newBlock.hash] = newBlock
        self.__latest_block = newBlock.hash

    def isValid(self):
        temp = self.__genesisBlock.prevHash
        for i in self.blockchain:
            curr = self.blockchain[i] 
            if curr.hash != curr.makeHash() and curr.hash != i:
                return False

            if temp == curr.prevHash:
                temp = curr.hash
            else:
                return False
        return True




