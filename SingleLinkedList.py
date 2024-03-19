class Node:
    def __init__(self, v, ptr = None):
        self.val = v
        self.next = ptr

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    #O(1)
    def add_first(self, e):
        if (self.head == None): #List is empty to start
            self.head = Node(e)
            self.tail = self.head
        else:
            tmp = Node(e)
            tmp.next = self.head
            self.head = tmp
            tmp = None #We're done with that pointer
        self.size += 1

    #O(1)
    def add_last(self, e):
        if (self.head == None): #List is empty to start
            self.head = Node(e)
            self.tail = self.head
        else:
            tmp = Node(e)
            tmp.next = None
            self.tail.next = tmp
            self.tail = tmp
        self.size += 1
       


    #O(n)
    def __str__(self):
        output = ""
        ptr = self.head
        while (ptr != None):
            output += str(ptr.val) + ","
            ptr = ptr.next
        return output

    def __len__(self):
        return self.size


#main
linkedList = SinglyLinkedList()
linkedList.add_first(1)
linkedList.add_first(2)
linkedList.add_first(3)
linkedList.add_last(1)
linkedList.add_last(2)
print(linkedList) #3 --> 3 --> 2 -->1 --> None