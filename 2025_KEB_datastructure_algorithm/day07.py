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

    def search(self, target):
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

def remove(self, target):
    if self.data == target:
        self.head = self.had.next
        return
    current = self.had
    previous = None
    while current:
        if current.data == target:
            previous.next = current.next
        else:
            previous = current
            current = current.next

if __name__ == "__main__":
    l = linkedlist()
    i = 0
    while i < 20:
        l.append(random.radint(a:1, b:20))
        l.append(n)
        print(n, end=' ')
        i = i + 1
        print(l)
        print(l.search(10))


