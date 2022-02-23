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
            return node
        if node.val < root.val:
            root.left = self.insert(root.left, node)        
        else:
            root.right = self.insert(root.right, node)
        return root

    def inorder(self, root) -> str:
        if root is None:
            return ''
        return '%s %s %s' % (self.inorder(root.left), root.val, self.inorder(root.right))
        

bst = BinaryTree()
# root insert
bst.root = bst.insert(bst.root, TreeNode(10))
bst.root = bst.insert(bst.root, TreeNode(8))
bst.root = bst.insert(bst.root, TreeNode(9))
bst.root = bst.insert(bst.root, TreeNode(-1))
bst.root = bst.insert(bst.root, TreeNode(100))
bst.root = bst.insert(bst.root, TreeNode(-5))
print(bst.inorder(bst.root))





        
# TODO:
# 1. insert
# 2. print tree (traversal)