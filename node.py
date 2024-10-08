class Node:
    def __init__(self, value = None, left = None, right = None) -> None:
        self.value = value
        self.left = left
        self.right = right

    def getChildren(self) -> list:
        children = []
        for child in [self.left, self.right]:
            if child:
                children.append(child)
        return children

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def __str__(self) -> str:
        return f"{self.value}"

    def __repr__(self) -> str:
        return self.__str__()

def get_tree() -> Node:
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    return a

def get_tree_numeral() -> Node:
    a = Node(3)
    b = Node(11)
    c = Node(4)
    d = Node(4)
    e = Node(2)
    f = Node(1)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    return a

def get_tree_numeral2() -> Node:
    a = Node(5)
    b = Node(11)
    c = Node(3)
    d = Node(4)
    e = Node(2)
    f = Node(1)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    return a

def main():
    a = get_tree()
    print(a)


if __name__ == "__main__":
    main()