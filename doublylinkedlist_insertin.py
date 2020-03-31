#node class for creating nodes
class Node:
    def __init__(self,data):
        self.next=None
        self.prev=None
        self.data=data
#doubly linkedlist class
class DoublyLinkedList:
    def __init__(self):
        self.head=None
    #function for pushing nodes into doubly linkedlist
    def push(self,newdata):
        newnode=Node(newdata)
        if self.head is None:
            self.head=newnode
            return
        newnode.next=self.head
        self.head.prev=newnode
        self.head=newnode
    #function for inserting a node after a given node in doubly linkedlist
    def insert_after(self,prevnode,newdata):
        if prevnode is None:
            print("given node is not present")
            return
        newnode=Node(newdata)
        newnode.next=prevnode.next
        prevnode.next=newnode
        newnode.prev=prevnode
        if newnode.next is not None:
            newnode.next.prev=newnode
    #function for inserting a node at the end of doubly linkedlist
    def append(self,newdata):
        newnode=Node(newdata)
        if self.head is None:
            self.head=newnode
            return
        lastnode=self.head
        while(lastnode.next is not None):
            lastnode=lastnode.next
        lastnode.next=newnode
        newnode.prev=lastnode
    #function for inserting a node before a given node in doubly linkedlist
    def insert_before(self,nextnode,newdata):
        if nextnode is None:
            return
        newnode=Node(newdata)
        newnode.prev=nextnode.prev
        nextnode.prev.next=newnode
        nextnode.prev=newnode
        newnode.next=nextnode   
    #function for printing doublylinkedlist in forward and reverse order
    def print_dllist(self):
        currentnode=self.head
        if currentnode is None:
            print("linkedlist is empty")
            return
        print("doublelinkedlist in forward order")
        while(currentnode is not None):
            last=currentnode
            print(currentnode.data)
            currentnode=currentnode.next
        print("doublelinkedlist in reverse order")
        while(last is not None):
            print(last.data)
            last=last.prev

if __name__=="__main__":
    dllist=DoublyLinkedList()
    dllist.push(4)
    dllist.push(3)
    dllist.push(2)
    dllist.push(1)
    #dllist.print_dllist()
    dllist.insert_after(dllist.head.next.next,3.5)
    #dllist.print_dllist()
    dllist.append(6)
    #dllist.print_dllist()
    dllist.insert_before(dllist.head.next,7)
    dllist.print_dllist()



        
