# Creating linked list.
# Linked list is made up of nodes, nodes contain data and a link to another node

# Creating a node
class Node:
    def __init__(self, data):
        self.data = data
        self.link = None


class LinkedList:
    # On creation of a linked list, the header will point to None as there are no nodes that exist
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("The Linked List is empty")
        else:
            print("Here are the values: ")
            n = self.head  # head references the node
            while n is not None:
                print(n.data)  # head points to first node which contains data
                n = n.link  # the node will have a link to the next node, so we change the pointer to that node

    # if you are adding the new node at the start of the list
    def add_at_beginning(self, data):
        new_node = Node(data)  # create a new node with the data
        new_node.link = self.head  # the new node will link to the previous first node (as we are adding to the start of the list), this link can be obtained from the head, as the head will point to the first node
        self.head = new_node  # since the new node will be the starting node, change the header to point to the new node

    # if you are adding the new node at the end of the list
    def add_at_end(self, data):
        new_node = Node(data)

        # If you are adding at end on an empty ll then the header should point to it, else add to end
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.link is not None:
                n = n.link
            n.link = new_node

    # adding new node after node (that matches value)
    def add_after(self, data, value):
        n = self.head
        if n is None:
            return print("There is no list")

        while n.data != value:
            if n.link is None and n.data != value:  # if we reached the end (last node link should be none, if data is not value then value did not exist in list)
                return print(value, " not found in list, cannot add ", data)
            else:
                n = n.link
        new_node = Node(data)
        new_node.link = n.link  # change the new node's link to be the previous nodes link (instead of A-->B, C-->B) with A as the value node, B as the next node and C as the new node
        n.link = new_node  # change node's link to be new node (instead of A-->B, A-->C, now it becomes A-->C-->B) with A as the value node, B ass the next node and C as the new node
        self.print_LL()

    # adding a new node before node (that matches value)
    def add_before(self, data, value):
        n = self.head
        if n is None:
            return print("There is no list")

        # if there is only one element
        elif n.link is None:
            if n.data != value:
                return print(value, " not found in list, cannot add ", data)
            else:
                new_node = Node(data)
                new_node.link = n
                self.head = new_node
                return self.print_LL()

        else:
            if n.data == value:
                new_node = Node(data)
                new_node.link = n
                self.head = new_node
                return self.print_LL()
            else:
                while n.data != value:
                    if n.link is None and n.data != value:
                        return print(value, " not found in list, cannot add ", data)
                    else:
                        m = n   # previous node
                        n = n.link
            new_node = Node(data)
            new_node.link = n  # new node's link is current node (instead of m-->n, C-->n) with m as previous node, n as value node and C as new node
            m.link = new_node  # previous node's link is now new node (instead of m-->n, m-->C, now it is m-->C-->n) with n as previous node, m as value node and C as new node
        self.print_LL()

    # delete first node
    def del_first(self):
        if self.head is None:
            print("Linked list is empty, delete first is impossible")
        else:
            self.head = self.head.link
        self.print_LL()

    # delete last node
    def del_last(self):
        if self.head is None:
            print("Linked list is empty, delete last is impossible")
        else:
            n = self.head
            # if there is only one node
            if n.link is None:
                self.head = None
            else:
                while n.link is not None:
                    m = n  # we will change m (which will end up as the 2nd last node)
                    n = n.link
                m.link = None
        self.print_LL()

    # delete node by the value
    def del_node_by_value(self, v):
        if self.head is None:
            print("Linked List is empty, delete at", v, "is impossible")
        else:
            if v == self.head.data:
                self.head = self.head.link
                return self.print_LL()

            n = self.head
            while n.link is not None:
                if v == n.link.data:
                    break
                n = n.link

            if n.link is None:
                print("Value not found")
            else:
                n.link = n.link.link

        self.print_LL()

"""
ll_1 = LinkedList()
ll_1.add_at_beginning(10)
ll_1.del_first()
ll_1.add_at_beginning(20)
ll_1.print_LL()
ll_1.add_after(15, 20)
ll_1.add_after(5, 15)
ll_1.print_LL()
ll_1.add_after(100, 50)

print("------------------")
ll_2 = LinkedList()
ll_2.add_at_end(10)
ll_2.add_at_end(20)
ll_2.print_LL()
ll_2.del_last()
ll_2.add_before(15, 10)
ll_2.add_before(20, 15)
ll_2.add_before(50, 20)
ll_2.add_before(1, 1)

print("------------------")
ll_3 = LinkedList()
ll_3.del_node_by_value(5)
ll_3.add_at_beginning(10)
ll_3.add_at_beginning(20)
ll_3.add_at_beginning(30)
ll_3.add_at_beginning(40)
ll_3.print_LL()
ll_3.del_node_by_value(30)
"""
