from node import Node, get_tree_numeral

def treeSumBFS(root: Node) -> int:
    if root == None:
        return 0
    
    res = 0
    queue = [root]
    while len(queue) > 0:
        current = queue.pop(0)
        res += current.value
        for child in current.getChildren():
            queue.append(child)

    return res

def treeSumDFS(root: Node) -> int:
    if root == None:
        return 0
    
    res = root.value
    for child in root.getChildren():
        res += treeSumDFS(child)

    return res

def main():
    root = get_tree_numeral()
    print(treeSumDFS(root))
    print(treeSumBFS(root))


if __name__ == "__main__":
    main()