class TreeNode:
    def __init__(self, val: int) -> None:
        self.left = None
        self.right = None
        self.val = val


class BinaryTree:
    def __init__(self) -> None:
        self.root = None
    
    def insert(self, root: TreeNode, node: TreeNode) -> TreeNode:
        if root is None:
            root = node
        else:
            if root.val <= node.val:
                if root.left is None:
                    root.left = node
                else: 
                    root.left = self.insert(root.left, node)
            else:
                if root.right is None:
                    root.right = node
                else:
                    root.right = self.insert(root.right, node)

            return root

    
    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        print (root.val)
        self.inorder(root.right)



bst = BinaryTree()
root = TreeNode(10)
bst.insert(root, TreeNode(8))
bst.insert(root, TreeNode(11))
bst.insert(root, TreeNode(9))
bst.insert(root, TreeNode(-1))
bst.insert(root, TreeNode(100))
bst.insert(root, TreeNode(-5))
print(bst.inorder(root))






        
# TODO:
# 1. insert
# 2. print tree (traversal)