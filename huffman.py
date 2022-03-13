import sys

#helper Node class for storing character and freq
class Node:
    def __init__(self, data):
        self.data = data
        self.freq = 0

#helper TreeNode class for construction of the tree
class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.right_child = None
        self.left_child = None

    def set_right_child(self, node):
        self.right_child = node
    
    def set_left_child(self, node):
        self.left_child = node

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def has_right_child(self):
        return self.right_child != None

    def has_left_child(self):
        return self.left_child != None

class Tree:
    def __init__(self, value=None):
        self.root = TreeNode(value)

    def get_root(self):
        return self.root

#Helper class to store the nodes in a list thats following an order like prio queue
class NodeList:
    def __init__(self):
        self.arr = list()
    
    def size(self):
        return len(self.arr)

    def add(self, node):
        if self.size() == 0:
            self.arr.append(node)
        else:
            last_node = self.arr[-1]
            if last_node.freq < node.freq:
                self.arr.append(node)
            else:
                self.arr.insert(-1, node)

    #helper method to show me the elements in the nodes list   
    def __repr__(self):
        pr_str = ''
        for idx, node in enumerate(self.arr):
            pr_str += '---node at index {}---\n'.format(idx)
            pr_str += node.data + '---'+ str(node.freq) + '\n'
            pr_str += '---------------------\n'
        return pr_str



def huffman_encoding(data):
    if data is None:
        return None
    data_cased = data.lower()
    data_list = NodeList()
    for chr in set(data_cased):
        data_node = Node(chr)
        data_node.freq = data.count(chr)
        data_list.add(data_node)
        

    print(data_list)
    return data_list
    pass

def huffman_decoding(data, tree):
    pass

if __name__ == "__main__":
    codes = {}
    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))
    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))


