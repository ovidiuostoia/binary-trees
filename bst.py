class BSTNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None
    
    
def insert(root: BSTNode, value) -> BSTNode:
    if not root:
        return BSTNode(value)
    
    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)
    return root

def minValueNode(root: BSTNode) -> BSTNode:
    # the min value node is the left-most node
    curr = root
    while curr and curr.left:
        curr = curr.left
    return curr

def remove(root: BSTNode, value) -> BSTNode:
    if not root:
        return None
    
    if value > root.value:
        root.right = remove(root.right, value)
    elif value < root.value:
        root.left = remove(root.left, value)
    else: # we found the node that will be removed
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else: # the node to be removed has two children
            minNode = minValueNode(root.right)              # find the min node from the right side
            root.value = minNode.value                      # replace the value to be removed with the min value from the right side
            root.right = remove(root.right, minNode.value)  # remove the min value node from the right side
    return root

def search(root: BSTNode, target: int) -> bool:
    if not root:
        return False
    
    if target < root.value:
        return search(root.left, target)
    elif target > root.value:
        return search(root.right, target)
    else:
        return True

def toString(root: BSTNode) -> None:
    if root.left:
        toString(root.left)
    print(root.value)
    if root.right:
        toString(root.right)

def main():
    a = BSTNode(5)
    b = BSTNode(6)
    c = BSTNode(1)
    a.left = c
    a.right = b

    print(search(a, 1)) # True
    print(search(a, 7)) # False
    # toString(a)

    root = insert(None, 4)
    insert(root, 2)
    insert(root, 6)
    insert(root, 5)
    insert(root, 7)
    toString(root)

    remove(root, 4)
    print("--------")
    toString(root)


if __name__ == "__main__":
    main()
