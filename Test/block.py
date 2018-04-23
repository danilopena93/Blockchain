import datetime as date
import hashlib
import json
import os

class Block(object):
    def __init__(self, dictionary):

        for k, v in dictionary.items():
            setattr(self, k, v)

        if not hasattr(self, 'nonce'):
            #We are throwing this in for generation
            self.nonce = None

        #In creating the first block, needs to be removed in future
        if not hasattr(self, 'hash'):
            self.hash = self.create_self_hash()

    def header_string(self):
        return str(self.index) + self.prev_hash + self.data + str(self.timestamp) + str(self.nonce)

    def create_self_hash(self):
        sha = hashlib.sha256()
        sha.update(self.header_string())
        return sha.hexdigest()

    def self_save(self):
        chaindata_dir = 'chaindata'
        #Front of zeros so they stay in numerical order
        index_string = str(self.index).zfill(6)

        filename = '%s/%s' % (chaindata_dir, index_string)

        with open(filename, 'w') as block_file:
            json.dump(self.__dict__(), block_file)

    #For printing purposes 
    def __dict__(self):
        info = {}
        info['Index'] = str(self.index)
        info['Timestamp'] = str(self.timestamp)
        info['Previous_Hash'] = str(self.prev_hash)
        info['Hash'] = str(self.hash)
        info['Data'] = str(self.data)

        return info
    
    #For printing purposes
    def __str__(self):
        return "Block <Previous Hash: {0}, Hash: {1}>".format(self.prev_hash, self.hash)

#Create first block
def create_first_block():
    #Index zero and arbitrary previous hash
    block_data = {}
    block_data['Index'] = 0
    block_data['Timestamp'] = date.datetime.now()
    block_data['Data'] = 'First Block Data'
    block_data['Previous_Hash'] = None
    block = Block(block_data)

    return block 

if __name__ == '__main__':
    #Data storage code
    #Check if chaindata folder exists
    chaindata_dir = 'chaindata/'
    if not os.path.exists(chaindata_dir):
        #Make the directory
        os.mkdir(chaindata_dir)

    #Check if dir is empty from just creation, or just empty before
    if os.listdir(chaindata_dir) == []:
        #Create first block
        first_block = create_first_block()
        first_block.self_save()



