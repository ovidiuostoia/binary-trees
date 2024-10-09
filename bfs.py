from node import Node

def bfs(src: Node) -> list:
    if src == None:
        return []
    
    res = []
    queue = [src]
    while len(queue) > 0:
        current = queue.pop(0)
        res.append(current)
        for child in current.getChildren():
            queue.append(child)

    return res

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

    print(bfs(a))


if __name__ == "__main__":
    main()
