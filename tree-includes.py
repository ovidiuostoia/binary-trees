from node import Node, get_tree

def treeIncludesBFS(root: Node, target: str) -> bool:
    if root == None:
        return False
    
    queue = [root]
    while len(queue) > 0:
        current = queue.pop(0)
        if current.value == target:
            return True
        for child in current.getChildren():
            queue.append(child)
    
    return False

def treeIncludesDFS(root: Node, target: str) -> bool:
    if root == None:
        return False
    if root.value == target:
        return True
    
    for child in root.getChildren():
        if treeIncludesDFS(child, target):
            return True

    return False

def main():
    a = get_tree()
    print(treeIncludesBFS(a, 'f')) # true
    print(treeIncludesBFS(a, 'j')) # false

    print(treeIncludesDFS(a, 'f')) # true
    print(treeIncludesDFS(a, 'j')) # false


if __name__ == "__main__":
    main()