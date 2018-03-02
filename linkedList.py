##Author: Rishabh Dalal
##Description: Node class and Linked list class

class Node:
    
    def __init__(self, nodeData):
        self.data = nodeData
        self.next = None

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data

    def setNext(self, newNext):
        self.next = newNext

    def getNext(self):
        return self.next

class LinkedList(object):

    def __init__(self):
        ##Constructor
        
        self._head = None
        self._tail = None
        self._size = 0
        self._current = None
        self._previous = None
        self._currentIndex = -1

    def search(self, targetItem):
        ##Search in both ordered and inordered linked list
        
        if self._current != None and self._current.getData() == targetItem:
            return True

        """
        UNCOMMENT FOR UNORDERED LIST
        self._previous = None
        self._current = self._head
        self._currentIndex = 0
        while self._current != None:
            if self._current.getData() == targetItem:
                return True
            else: #inch-worm down list
                self._previous = self._current
                self._current = self._current.getNext()
                self._currentIndex += 1
        return False
        """
        self._previous = None
        self._current = self._head
        self._currentIndex = 0
        while self._current != None:
            if self._current.getData() == targetItem:
                return True
            elif self._current.getData() > targetItem:
                return False
            else: 
                self._previous = self._current
                self._current = self._current.getNext()
                self._currentIndex += 1
        return False

    def add(self, newItem, skip = False):
        ##Adding only if unavaiable in linked list
        
        if self.search(newItem):
            return
        """
        UNCOMMENT FOR UNORDERED LIST
        temp = Node(newItem)
        if self._size == 0:
            self._tail = temp
        else:
            temp.setNext(self._head)
        self._head = temp
        self._size += 1
        """
        if skip:
            temp = SkippedNode(newItem)
        else:
            temp = Node(newItem)
 
        if self._previous == None:
            self._head = temp
        else:
            self._previous.setNext(temp)
        temp.setNext(self._current)
        self._size += 1
        if self._current == None:
            self._tail = temp
        self._current = None
                

    def remove(self, item):
        ##Removing item form linked list if in it. Else an error
        
        if not self.search(item):
            raise ValueError("Cannot remove item since it is not in the list!")

        if self._current == self._tail:
            self._tail = self._previous
            
        if self._current == self._head:
            self._head = self._head.getNext()
        else:
            self._previous.setNext(self._current.getNext())
        self._current = None
        self._size -= 1

    def isEmpty(self):
        ##Checking to see if the linked list is empty
        
        return self._size == 0

    def length(self):
        ##Returning length of linked list
        
        return self._size

    def append(self, newItem):
        ## Adding item to the head of linked list if not in list
        
        if self.search(newItem):
            raise ValueError("Item already in the list!")
   
        temp = Node(newItem)
        if self._size == 0:
            self._head = temp
        else:
            self._tail.setNext(temp)
        self._tail = temp
        self._size += 1

    def index(self, item):
        ##Returning index of an item in the list, if in it.
        
        if not self.search(item):
            raise ValueError("Cannot determine index since item is not in the list!")

        return self._currentIndex


    def insert(self, pos, newItem):
        ##Inserts an item in a given position for an unordered list
        if not isinstance(pos, int):
            raise TypeError("Position must be an integer!")
        
        if pos < 0 or pos >= self._size:
            raise IndexError("Cannot insert because index", pos, "is invalid!")

        if self.search(newItem):
            raise ValueError("Cannot insert because item is already in the list!")
        
        temp = Node(newItem)

        self._current = self._head
        self._previous = None
        for count in range(pos):
            self._previous = self._current
            self._current = self._current.getNext()
            
        temp.setNext(self._current)
        if self._current == self._head:
            self._head = temp
        else:
            self._previous.setNext(temp)
        self._current = None
        self._size += 1


    def pop(self, pos = None):
        ##Removing last item of the list
        
        if pos == None:
            pos = self._size - 1
        
        if not isinstance(pos, int):
            raise TypeError("Position must be an integer!")
        
        if pos >= self._size or pos < 0:
            raise IndexError("Cannot pop from index", pos, "-- invalid index!")

        self._current = self._head
        self._previous = None
        for count in range(pos):
            self._previous = self._current
            self._current = self._current.getNext()
            
        if self._current == self._tail:
            self._tail = self._previous
            
        if self._current == self._head:
            self._head = self._head.getNext()
        else:
            self._previous.setNext(self._current.getNext())
        returnValue = self._current.getData()
        self._current = None
        self._size -= 1
        return returnValue

    def __str__(self):
        ##Printing the linked list
        
        resultStr = "(head)"
        current = self._head
        while current != None:
            resultStr += " " + str(current.getData())
            current = current.getNext()
        return resultStr + " (tail)"
    
    def __iter__(self):
        ##Iterating over the linked list
        
        current = self._head
        while current:
            yield current.getData()
            current = current.getNext()


