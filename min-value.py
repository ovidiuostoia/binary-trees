from node import Node, get_tree_numeral

def minValueBFS(root: Node) -> int:
    if root == None:
        return 0
    
    min = root.value
    queue = [root]
    while len(queue) > 0:
        current = queue.pop()
        if min > current.value:
            min = current.value
        for child in current.getChildren():
            queue.append(child)

    return min

def minValueDFS(root: Node) -> int:
    if root == None:
        return 0
    
    smallest = root.value
    for child in root.getChildren():
        smallest = min(smallest, minValueDFS(child))
    
    return smallest

def main():
    a = get_tree_numeral()
    print(minValueBFS(a)) # 1
    print(minValueDFS(a)) # 1


if __name__ == "__main__":
    main()

