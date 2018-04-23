from flask import Flask
from block import Block
import sync
import json
#Displaying the blockchain
node = Flask(__name__)

#Initial blocks that are synced 
node_blocks = sync.sync()
@node.route('/blockchain.json', methods = ['GET'])
def blockchain():
    """
    Shoots back the blockchain, which in our case, is a json
    list of hashes with the block information which is:
    index
    timestamp
    data
    hash
    prev_hash
    """
    #Regrab the nodes if they have changed
    node_blocks = sync.sync()

    python_blocks = []
    for block in node_blocks:
        python_blocks.append(block.__dict__())

    json_blocks = json.dumps(python_blocks)

    return json_blocks

if __name__ == '__main__':
    node.run()