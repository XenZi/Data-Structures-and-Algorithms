class TreeNode():
    def __init__(self, data) -> None:
        self.data = data
        self.parent = None
        self.children = []

    def is_root(self):
        return self.parent is None
    
    def is_leaf(self):
        return len(self.children) == 0
    
    def add_child(self, x):
        self.children.append(x)
        x.parent = self
    
    def __str__(self) -> str:
        return str(self.data)

    
class Tree():
    def __init__(self) -> None:
        self.root = None
    
    def is_empty(self):
        return self.root is None

    def depth(self, x):
        if x.is_root():
            return 0
        else:
            1 + self.depth(x.parent)
        
    def _height(self, x):
        if x.is_leaf():
            return 0
        return 1 + max(self._height(ch) for ch in x.children)
    
    def height(self):
        return self._height(self.root)
    
    def preorder(self, x, func):
        if not self.is_empty():
            func(x.data)
            for ch in x.children:
                self.preorder(ch, func)
    
    def postorder(self, x):
        if not self.is_empty():
            for ch in x.children:
                self.postorder(ch)
            print(x)
    
if __name__ == "__main__":
    t = Tree()
    t.root = TreeNode(0)
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)

    t.root.add_child(a)
    t.root.add_child(b)
    a.add_child(c)
    a.add_child(d)
    c.add_child(e)
    print(f'Dubina cvora: {str(t.depth(t.root))}')
    print(f'Visina stabla {str(t.height())}')
