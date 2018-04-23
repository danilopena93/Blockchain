import os
import json
from block import Block

#Sync node 
def sync():
    node_blocks = []
    #We are assuming that the folder and at least the initial block exists
    chaindata_dir = 'chaindata'

    if os.path.exists(chaindata_dir):
        for filename in os.listdir(chaindata_dir):
            if filename.endswith('.json'):
                filepath = '%s/%s' % (chaindata_dir, filename)
                with open(filepath, 'r') as block_file:
                    block_info = json.load(block_file)

                    #Since we can init a Block with just a dictionary
                    block_object = Block(block_info)

                    node_blocks.append(block_object)

    return node_blocks