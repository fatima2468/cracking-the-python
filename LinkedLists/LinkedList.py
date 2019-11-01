class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head:Node = None

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        curr = self.head
        if not self.head:
            self.head = new_node
        else:
            while curr.next:
                curr = curr.next
            curr.next = new_node

    def show(self):
        current = self.head
        while current:
            print(f"{current.data} -> " if current.next else current.data, end="")
            current = current.next


l1 = LinkedList()
l1.insert_at_start(1)
l1.insert_at_start(2)
l1.insert_at_start(3)
l1.show()
print()

l2 = LinkedList()
l2.insert_at_end(1)
l2.insert_at_end(2)
l2.insert_at_end(3)
l2.show()















