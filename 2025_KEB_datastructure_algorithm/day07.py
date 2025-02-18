import self


def def__init__(self, data, next):
    pass


class Node:
    def__init__(self, data, next=None)
    self.data = data
    self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
         if not self.head:
             self.head = Node(data)
             return

    def search(self, targt):
        current = self.head
        while current.next:
            if current.data == target:
                return True
            else:
                current = current.next
                return False

    while current.next: # if next node exist
        current = current.next
    current.next = Node(next)

def __str__(self):
    node = self.head
    while node is not None:
        print(node.data)
        node = node.next
    return "end"

if __name__ == "__main__"
    l = linkedlist()
    l.append(7)
    l.append(-11)
    l.append(8)
