# Question 1: Implementing a Stack

class Stack:
    """
    Design a Python class named `Stack` to represent a stack data structure.

    Theory:
    A stack is a linear data structure that follows the Last In, First Out (LIFO) principle. 
    It has two main operations: push and pop.
    - Push: Adds an element to the top of the stack.
    - Pop: Removes and returns the top element from the stack.

    Operations:
    1. Push: Add an element to the top of the stack.
    2. Pop: Remove and return the top element from the stack.
    3. Peek: Return the top element of the stack without removing it.
    4. Is Empty: Check if the stack is empty.
    5. Size: Return the number of elements in the stack.

    Test Cases:
    Test Case 1:
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.peek() == 3
    assert stack.pop() == 3
    assert stack.size() == 2
    assert stack.is_empty() is False

    Test Case 2:
    stack = Stack()
    assert stack.is_empty() is True
    stack.push("A")
    stack.push("B")
    stack.push("C")
    assert stack.pop() == "C"
    assert stack.peek() == "B"
    assert stack.size() == 2
    assert stack.is_empty() is False
    """

    __MAX_SIZE = 6
    def __init__(self):
        self.sList =[]
    @property
    def isEmpty(self):
        return True if len(self.sList)==0 else False
    def push(self, item):
        if len(self.sList) == Stack.__MAX_SIZE:
            print('Stack Overflow')
            return False
        else:
            self.sList.insert(0,item)
            return True
        
    def pop(self):
        if not self.isEmpty:
            s = f'{self.sList[0]} Remove from stack'
            t = self.sList[0]
            self.sList.pop(0)
            return t
        else:
            return 'Stack Underflow'
    
    @property
    def peek(self):
        if not self.isEmpty:
            return self.sList[0]
        else:
            return 0
    @property
    def size(self):
        return len(self.sList)


# Question 2: Implementing a Queue

class Queue:
    """
    Design a Python class named `Queue` to represent a queue data structure.

    Theory:
    A queue is a linear data structure that follows the First In, First Out (FIFO) principle. 
    It has two main operations: enqueue and dequeue.
    - Enqueue: Adds an element to the rear of the queue.
    - Dequeue: Removes and returns the front element from the queue.

    Operations:
    1. Enqueue: Add an element to the rear of the queue.
    2. Dequeue: Remove and return the front element from the queue.
    3. Front: Return the front element of the queue without removing it.
    4. Is Empty: Check if the queue is empty.
    5. Size: Return the number of elements in the queue.

    Test Cases:
    Test Case 1:
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.front() == 1
    assert queue.dequeue() == 1
    assert queue.size() == 2
    assert queue.is_empty() is False

    Test Case 2:
    queue = Queue()
    assert queue.is_empty() is True
    queue.enqueue("A")
    queue.enqueue("B")
    queue.enqueue("C")
    assert queue.dequeue() == "A"
    assert queue.front() == "B"
    assert queue.size() == 2
    assert queue.is_empty() is False
    """
    __MAX_SIZE = 6
    def __init__(self):
        self.lQueue = []

    def enqueue(self, item):
        if len(self.lQueue)==Queue.__MAX_SIZE:
            raise 'Queue Overflow!'
            
        else:
            self.lQueue.insert(0,item)
            return True
        # Add an element to the rear of the queue
        #pass

    @property
    def dequeue(self):
        # Remove and return the front element from the queue
        if self.is_empty:
            raise 'Queue is Underflow'
        else:
            t = self.lQueue[-1]
            self.lQueue.pop(-1)
            return t
    
    @property
    def front(self):
        if self.is_empty:
            return 'None'
        else:
            return self.lQueue[-1]
        # Return the front element of the queue without removing it
        # pass
    
    @property
    def is_empty(self):
        if len(self.lQueue) ==0:
            return True
        else:
            return False

    @property
    def size(self):
        return len(self.lQueue)
