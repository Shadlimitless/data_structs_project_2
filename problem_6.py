class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # In union we need to find all unique elements in both linked lists
    # Flat is better than nested (Zen of python) . The computation time complexity here is O(n)
    list1_node = llist_1.head
    list2_node = llist_2.head
    # Using set so as to have only unique values
    union_set = set()
    while list1_node:
        union_set.add(list1_node.value)
        list1_node = list1_node.next
    while list2_node:
        union_set.add(list2_node.value)
        list2_node = list2_node.next
    union_list = LinkedList()
    for item in union_set:
        union_list.append(item)
    return union_list
    pass

def intersection(llist_1, llist_2):
    # Your Solution Here
    # In intersection we need to find elements only in both of them
    # Computation time complexity here is O(n) as the input size affects due to the loops
    list1_node = llist_1.head
    list2_node = llist_2.head
    intersection_set = set()
    while list1_node:
        intersection_set.add(list1_node.value)
        list1_node = list1_node.next
    result_set = set()
    while list2_node:
        if list2_node.value in intersection_set:
            result_set.add(list2_node.value)
        list2_node = list2_node.next
    result = LinkedList()
    for item in result_set:
        result.append(item)    
    return result
    pass


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))
# Will not print anything since there is no elements both in list 3 and list 4

