import sys

#helper Node class for storing character and freq
class Node:
    def __init__(self, data):
        self.data = data
        self.freq = 1

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


def huffman_encoding(data):

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

huffman_encoding("AAAAAAABBBCCCCCCCDDEEEEEE")
