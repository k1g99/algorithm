class Node:
    def __init__(self, d):
        self.data = d
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, val):
        node = Node(val)
        if(self.head is None):
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next

    def show(self):
        ptr = self.head
        s = ""
        while (ptr != None):
            s += str(ptr.data)
            s += " "
            ptr = ptr.next
        print(s)

    def find(self, val):
        ptr = self.head
        while (ptr != None):
            if(ptr.data == val):
                return ptr
            ptr = ptr.next
        return None

    def removeNth(self, idx):
        if(idx == 1):
            self.head = self.head.next
        else:
            before = self.head
            for i in range(idx - 2):
                before = before.next
            before.next = before.next.next
            if(before.next == None):
                self.tail = before


ll = LinkedList()
for i in range(10):
    ll.add(i)
ll.show()

for i in range(10):
    ll.removeNth(1)
ll.show()

ll.add(1)
ll.add(2)

ll.show()