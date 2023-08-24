class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
    def insertionll(self,data):
        newnode = Node(data)
        if self.head:
            cur_node = self.head
            while cur_node.next!=None:
                cur_node = cur_node.next
            cur_node.next=newnode
        else:
            self.head = newnode
    def printlist(self):
        cur = self.head
        while cur is not None:
            print(cur.data,end='-->')
            cur = cur.next




linklist = LinkedList()
#linklist.head = Node(3)
linklist.insertionll(4)
linklist.insertionll(5)
linklist.insertionll(6)
linklist.insertionll(8)
linklist.printlist()




