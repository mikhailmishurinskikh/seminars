class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    def append(self, value):
        if self.next != None:
            self.next.append(value)
        else:
            self.next = Node(value)
            self.next.prev = self
class List:
    def __init__(self, first, *args):
        self.first = Node(first)
        self.last = self.first
        for i in args:
            self.last.append(i)
            self.last = self.last.next
    def insert(self, value, k): #before k_node
        k_node = self.first
        for i in range(k):
            k_node = k_node.next
        new_node = Node(value)
        new_node.prev = k_node.prev
        new_node.prev.next = new_node
        new_node.next = k_node
        k_node.prev = new_node 
    def get(self, k):
        if k >= 0:
            k_node = self.first
            for i in range(k):
                k_node = k_node.next
            return k_node.data
        else:
            k_node = self.last
            for i in range(-k-1):
                k_node = k_node.prev
            return k_node.data
    def pop(self, k):
        if k >= 0:
            k_node = self.first
            for i in range(k):
                k_node = k_node.next
        else:
            k_node = self.last
            for i in range(-k-1):
                k_node = k_node.prev
        k_node.next.prev = k_node.prev
        k_node.prev.next = k_node.next
        return k_node.data
    def __len__(self):
        k_node = self.first
        i = 0
        while k_node.next != None:
            k_node = k_node.next
            i+=1
        return i+1
    def __str__(self):
        List_str = str(self.first.data)
        k_node = self.first
        for i in range(len(self)-1):
            List_str += f', {k_node.next.data}'
            k_node = k_node.next
        return List_str
def check():
    List1 = List(1, 2, 3, 4, 8 ,5, 4, 3, 2)
    print(List1)
    print(List1.get(5))
    print(List1.get(-2))
    List1.insert(151, 4)
    print(List1)
    List1.pop(6)
    print(List1)
    print(len(List1))
if __name__ == '__main__':
   check()
