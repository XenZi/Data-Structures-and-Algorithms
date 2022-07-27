'''
    Stack:
        - LIFO principle (last-in-first-out)
        - main operations:
            - push(el) - pushes element on top
            - pop() - pops out the last elemenet
        - additional operations:
            - top() - returns last element
            - len() - returns actual length of Stack
            - is_empty() - helps us in defining edge cases
        
        - Big O - O(1) - constant operations
'''


class Stack:
    def __init__(self) -> None:
        self._data = []   

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0
    
    def top(self):
        return self._data[len(self._data) - 1]
    
    def push(self, object):
        self._data.append(object)
    
    def pop(self):
        if self.is_empty():
            raise Exception("Error") 
        el = self.top()
        self._data.pop()
        return el

    def __str__(self) -> str:
        return " ".join(str(x) for x in self._data)
    

stack = Stack()


stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()
print(stack.is_empty())
print(stack)
