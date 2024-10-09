from node import Node, get_tree

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
    a = get_tree()

    print(bfs(a))


if __name__ == "__main__":
    main()
