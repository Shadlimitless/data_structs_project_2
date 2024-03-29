from base64 import encode
from logging import root
import sys

#helper Node class for storing character and freq

class Node:
    def __init__(self, data=None):
        self.data = data
        self.freq = 0
        self.huff_code = ""
        self.left_child = None
        self.right_child = None

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

    def set_binary_code(self, code):
        # print(code)
        if self.huff_code is None:
            self.huff_code = code
        else:
            self.huff_code += code

    def __repr__(self):
        return str(self.data)+ ", "+str(self.freq)+", "+self.huff_code


class Tree:
    def __init__(self, value=None):
        self.root = value

    def get_root(self):
        return self.root   

    # Tree method that calculates the binary code for each character, and returns a dictionary with index , node pairs so that I can easily access them later
    def generate_binarycodes(self):
        data_dict = dict()
        def _generate_binarycodes(node, encoding):
            if not node.has_left_child() and not node.has_right_child():
                node.set_binary_code(encoding)
                data_dict[node.data] = node
                return 
            if node.has_left_child():
                # print('pass left')
                _generate_binarycodes(node.get_left_child(), encoding = encoding + "0")
            if node.has_right_child():
                # print('pass right')
                _generate_binarycodes(node.get_right_child(), encoding = encoding + "1")                                        
        encoding = str()
        root = self.get_root()
        _generate_binarycodes(root, encoding)
        # print("The encoding is {}".format(data_dict))
        return data_dict

#Helper class to store the nodes in a list thats following an order like prio queue
class NodeList:
    def __init__(self):
        self.arr = list()
    
    def size(self):
        return len(self.arr)

    # Method used to calculate where to add new node in the list based on frequency
    def add(self, node):
        if self.size() == 0:
            self.arr.append(node)
        else:
            for idx, el in enumerate(self.arr):
                if el.freq > node.freq:
                    self.arr.insert(idx, node)
                    return
            self.arr.append(node)

    # Method used to reinsert nodes with summed up frequency
    def reinsert(self, first_node, second_node, idx=None):
        new_node = Node()
        new_node.freq = first_node.freq + second_node.freq
        new_node.set_left_child(first_node)
        new_node.set_right_child(second_node)
        if idx is None:
            self.arr.append(new_node)
        else:
            self.arr.insert(idx, new_node)

    def pop(self, idx=None):
        if idx is None:
            return self.arr.pop()
        return self.arr.pop(idx)

    #helper method to show me the elements in the nodes list   
    def __repr__(self):
        pr_str = ''
        for idx, node in enumerate(self.arr):
            pr_str += '---node at index {}---\n'.format(idx)
            pr_str += '-----'+str(node.data)+"---"+str(node.freq)+'--'+str(node.huff_code)+'\n'
        return pr_str



def huffman_encoding(data):
    if data is None or len(data) == 0:
        return -1, -1
    data_list = NodeList()
    #Create ordered lists of the chars and their freq
    for chr in set(data):
        data_node = Node(chr)
        data_node.freq = data.count(chr)
        data_list.add(data_node)
    # print("first: {}".format(data_list))
    # Initialising root node
    root_node = Node()
    # If there was only one letter then the data_list will have only one node in it and the loop to sum up the nodes will break
    if data_list.size() > 1:
        while True:
            # Need to know if i'm remaining with last two items in list with uncombined sums
            if data_list.size()>3:
                first_node = data_list.pop(0)
                second_node = data_list.pop(0)
                data_list.reinsert(first_node, second_node, 0)
            else:
                second_node = data_list.pop()
                first_node = data_list.pop()
                data_list.reinsert(first_node, second_node)
                break

        # Get the calculated nodes and use them to create root
        left_child = data_list.pop(0)
        right_child = data_list.pop(0)
        root_node.freq = left_child.freq + right_child.freq
        root_node.set_left_child(left_child)
        root_node.set_right_child(right_child)
    else:
        left_child = data_list.pop()
        root_node.freq = left_child.freq
        root_node.set_left_child(left_child) 
    tree = Tree(root_node)
    # print("Here: {}".format(data_list))
    # Call tree method that calculates binary code for each letter
    data_dict = tree.generate_binarycodes()
    # Finally generate the full binary code for the whole string
    encoding = ""
    for chr in data:
        node = data_dict[chr]
        encoding = encoding + node.huff_code
    return encoding, tree


def huffman_decoding(data, tree):
    decoded_list = []
    # Initialise node variable to be used in bit loop to get the characters
    node = tree.get_root()
    for bit in data:
        if bit == "0":
            child_node = node.get_left_child()
        else:
            child_node = node.get_right_child()
        # If it doesnt have children its a leaf node, hence get the data, else move to the child
        if not child_node.has_left_child() and not child_node.has_right_child():
            decoded_list.append(child_node.data)
            node = tree.get_root()
        else:
            node = child_node
    # print(decoded_list)      
    return "".join(decoded_list)




def test_func(data):
    encoded_data, tree = huffman_encoding(data)
    if encoded_data == -1:
        print("No data to encode!")
    else:
        print("The size of the data is: {}\n".format(sys.getsizeof(data)))
        print("The content of the data is: {}\n".format(a_great_sentence))
        print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print("The content of the encoded data is: {}\n".format(encoded_data))

        decoded_data = huffman_decoding(encoded_data, tree)
        print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print("The content of the encoded data that has been decoded is: {}\n".format(decoded_data))



if __name__ == "__main__":
    # Test normal scenario
    a_great_sentence = "There is a tree"
    test_func(a_great_sentence)
    # Test edge case with same letter
    a_great_sentence = "AAAAAAA"
    test_func(a_great_sentence)
    # Test edge case with empty str/data
    test_func("")
