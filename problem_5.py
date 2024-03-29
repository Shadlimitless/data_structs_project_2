import hashlib
import datetime

class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = self.data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def __repr__(self):
        return str(self.timestamp)+", "+self.data+", "+self.hash

# Blockchain class that works like a linkedlist

class Blockchain:

    def __init__(self):
        self.head = None

    def put(self, data):
        if len(data) == 0:
            print("Cannot create a block with empty data")
            return 
        new_block = Block(datetime.datetime.now(), data, 0)
        if self.head is None:
            self.head = new_block
            return
        block = self.head
        new_block.previous_hash = block
        self.head = new_block

    def calc_hash(self, data):
        data_str = str(data)
        sha = hashlib.sha256()
        hash_str = data_str.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def __repr__(self):
        print_out = str()
        block = self.head
        while block:
            print_out += '---------------\n'
            print_out += str(block.timestamp)+", "+block.data+", "+block.hash + '\n'
            print_out += '---------------\n'
            block = block.previous_hash
        return print_out   


# Examples of adding info to the blockchain and printing out the results
chain = Blockchain()
chain.put("my temp")
chain.put("another one")
chain.put("last one")
chain.put("")
print(chain)
# Expected output is each block, starting with the last one since its last to get in


    