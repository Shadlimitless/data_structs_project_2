import sys

#helper Node class for storing character and freq
class Node:
    def __init__(self, data=None):
        self.data = data
        self.freq = 0
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

    
#helper TreeNode class for construction of the tree
class TreeNode(Node):
    def __init__(self, freq_sum=None):
        self.freq = freq_sum



    

class Tree:
    def __init__(self, value=None):
        self.root = value

    def get_root(self):
        return self.root

    def generate_binarycodes(self):
        def _generate_binarycodes(node, encoding):
            if node is None:
                return ""
            if node.has_left_child():
                print('pass left')
                encoding = _generate_binarycodes(node.get_left_child(), encoding)
                if encoding is None:
                    encoding = "0"
                else:
                    encoding += "0"
            if node.has_right_child():
                print('pass right')
                print("1")
                encoding = _generate_binarycodes(node.get_right_child(), encoding)
                if encoding is None:
                    encoding = "1"
                else:
                    encoding += "1"
                            
        encoding = str()
        root = self.get_root()
        _generate_binarycodes(root, encoding)
        print("The encoding is {}".format(encoding))
        return encoding

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

    def reinsert(self, node, idx=None):
        if idx is None:
            self.arr.append(node)
        else:
            self.arr.insert(idx, node)

    def pop(self, idx=None):
        if idx is None:
            return self.arr.pop()
        return self.arr.pop(idx)

    #helper method to show me the elements in the nodes list   
    def __repr__(self):
        pr_str = ''
        for idx, node in enumerate(self.arr):
            pr_str += '---node at index {}---\n'.format(idx)
            if type(node) == Node:
                pr_str += node.data + '---'+ str(node.freq) + '\n'
            else:
                pr_str += '-----'+str(node.freq)+'----\n'
            pr_str += '---------------------\n'
        return pr_str



def huffman_encoding(data):
    if data is None:
        return None
    data_cased = data.lower()
    data_list = NodeList()
    #Create ordered lists of the chars and their freq
    for chr in set(data_cased):
        data_node = Node(chr)
        data_node.freq = data_cased.count(chr)
        data_list.add(data_node)
    #Create tree for generating binary code
    print(data_list)
    while True:
        # Need to know if i'm remaining with last two items in list with uncombined sums
        if data_list.size()>3:
            first = data_list.pop(0)
            second = data_list.pop(0)
            sum = first.freq + second.freq
            new_node = TreeNode(sum)
            new_node.set_left_child(first)
            new_node.set_right_child(second)
            data_list.reinsert(new_node, 0)
        else:
            second = data_list.pop()
            first = data_list.pop()
            sum = first.freq + second.freq
            new_node = TreeNode(sum)
            new_node.set_left_child(first)
            new_node.set_right_child(second)
            data_list.reinsert(new_node)
            break

    # Get the calculated nodes and use them to create root
    left_child = data_list.pop(0)
    right_child = data_list.pop(0)
    root_node = TreeNode(left_child.freq + right_child.freq)
    root_node.set_left_child(left_child)
    root_node.set_right_child(right_child)
    tree = Tree(root_node)
    
    return tree.generate_binarycodes(), tree
    pass

def huffman_decoding(data, tree):
    pass

if __name__ == "__main__":
    codes = {}
    a_great_sentence = "AAAAAAABBBCCCCCCCDDEEEEEE"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))
    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))


