from node import Node

def dfsPrint(src: Node) -> None:
    if src == None:
        return
    
    stack = [src]
    while len(stack) > 0:
        current = stack.pop()
        print(current)
        for child in current.getChildren():
            stack.append(child)


def dfsrPrint(src: Node) -> None:
    if src == None:
        return
    
    print(src)
    for child in src.getChildren():
        dfsrPrint(child)

def dfs(src: Node) -> list:
    if src == None:
        return []
    
    res = []
    stack = [src]
    while len(stack) > 0:
        current = stack.pop()
        res.append(current)
        for child in current.getChildren():
            stack.append(child)
            
    return res

def dfsr(src: Node) -> list:
    if src == None:
        return []
    
    left = dfsr(src.left)
    right = dfsr(src.right)
    return [src, *left, *right]

def main():
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

    # print("DFS Traversal:")
    # dfsPrint(a)  # acfbed

    # print("\nDFS Recursive Traversal:")
    # dfsrPrint(a) # abdecf

    print(dfs(a))
    print(dfsr(a))


if __name__ == "__main__":
    main()
