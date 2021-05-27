from package.chain import Blockchain

if __name__ == '__main__':
    chain = Blockchain()
    chain.addBlock({"name":"Prathamesh"})
    chain.addBlock("whhiufia")
    print(chain.blockchain)