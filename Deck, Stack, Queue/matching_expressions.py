class Stack:

    def __init__(self):
        self._data = []
    
    def __len__(self):
        return len(self._data)
    
    def top(self):
        return self._data[-1]
    
    def is_empty(self):
        return len(self._data) == 0
    
    def push(self, el):
        return self._data.append(el)
    
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty broh")
        return self._data.pop()

def is_matching(expression):
    left_side = "([{"
    right_side = ")]}"

    stack = Stack()

    for char in expression:         # for za svaki character u expressionu
        if char in left_side:       # ukoliko je char otvorena zagrada, ona se nalazi u stringu left_side
            stack.push(char)        # ako je uslov ispunjen, u stack prebaciti char
        elif char in right_side:    # ukoliko je char zatvorne zagrada
            if stack.is_empty():    # ukoliko je stack prazan, odnosno vise nema znakova, stack je false
                return False
            if right_side.index(char) != left_side.index(stack.pop()):
                return False
    return stack.is_empty() # ako je stack prazan, uslov je ispunjen i onda je True

if __name__ == "__main__":
    print(is_matching("{[2+3] * ([5+3]}"))