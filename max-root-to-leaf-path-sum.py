import sys
from node import Node, get_tree_numeral2

def maxRootToLeafPathSum(root: Node) -> int:
    if root == None:
        return -sys.maxsize
    
    res = 0
    for child in root.getChildren():
        res = max(res, maxRootToLeafPathSum(child))

    return root.value + res

def main():
    a = get_tree_numeral2()
    print(maxRootToLeafPathSum(a))


if __name__ == "__main__":
    main()