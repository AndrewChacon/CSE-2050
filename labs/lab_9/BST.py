class BSTNode:
    def __init__(self, data, parent = None):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None: self.root = BSTNode(data)
        else: self._add_child(data, self.root)


    def _add_child(self, data, p_node):
        if data == p_node.data: #duplicate items cannot be added
            return

        if data < p_node.data:
            if p_node.left is not None: self._add_child(data, p_node.left)
            else: p_node.left = BSTNode(data, p_node)

        else:
            if p_node.right is not None: self._add_child(data, p_node.right)
            else: p_node.right = BSTNode(data, p_node)
            
    def get_max(self):
        if self.root: return self._get_right_child(self.root)

    def _get_right_child(self, node):
        if node.right: return self._get_right_child(node.right)
        return node.data

    def get_min(self):
        if self.root: return self._get_left_child(self.root)

    def _get_left_child(self, node):
        if node.left: return self._get_left_child(node.left)
        return node.data

    def traverse_in_order(self, node, traversed_data):
        if node:
            self.traverse_in_order(node.left, traversed_data)
            traversed_data.append(node.data)
            self.traverse_in_order(node.right, traversed_data)

    def delete(self, data):
        if self.root: self._remove_node(data, self.root)

    def _remove_node(self, data, node):
        if node is None: return
        if data < node.data: self._remove_node(data, node.left)
        elif data > node.data: self._remove_node(data, node.right)
        else: 
            if  node.right is None and node.left is None:
                parent = node.parent

                if parent is not None:
                    if parent.right == node: parent.right = None
                    if parent.left == node: parent.left = None
                else: self.root = None
                del node
            elif node.right is not None and node.left is None:
                parent = node.parent
                if parent is not None:
                    if parent.right == node: parent.right = node.right
                    if parent.left == node: parent.left = node.right
                else: self.root = node.right
                node.right.parent = parent
                del node
            elif  node.left is not None and node.right is None:
                parent = node.parent
                if parent is not None:
                    if parent.right == node: parent.right = node.left
                    if parent.left == node: parent.left = node.left
                else: self.root = node.left
                node.left.parent = parent
                del node
            else:
                predecessor = self._get_predecessor(node.left)
                predecessor.data, node.data = node.data, predecessor.data
                self._remove_node(data, predecessor)
        pass

    def _get_predecessor(self, node):
        if node.right:
            return self._get_predecessor(node.right)
        return node

    def traverse_pre_order(self, node, traversed_data):
        if node:
            traversed_data.append(node.data)
            self.traverse_pre_order(node.left, traversed_data)
            self.traverse_pre_order(node.right, traversed_data)

    def traverse_post_order(self, node, traversed_data):
        if node:
            self.traverse_post_order(node.left, traversed_data)
            self.traverse_post_order(node.right, traversed_data)
            traversed_data.append(node.data)



if __name__ == "__main__":
    BST = BinarySearchTree()

    random_data = [12, 4, 20, 8, 1, 16, 27]
    for data in random_data:
        BST.insert(data)

    print("Testing Max...")
    assert(BST.get_max() == 27)
    print("PASSED!")

    print()
    print("Testing Min...")
    assert(BST.get_min() == 1)
    print("PASSED!")

    print()
    print("Testing In-order Traversal...")
    traversed_data = []
    BST.traverse_in_order(BST.root, traversed_data)
    assert(traversed_data == [1, 4, 8, 12, 16, 20, 27])
    print("PASSED!")

    print()
    print("Testing Deletion of root node with two child...")
    BST.delete(12)
    traversed_data = []
    BST.traverse_in_order(BST.root, traversed_data)
    assert(traversed_data == [1, 4, 8, 16, 20, 27])
    print("PASSED!")

    print()
    print("Checking new root after deletion...")
    assert(BST.root.data == 8)
    print("VERIFIED!")

    ########## Task2 ##########
    print()
    print("########## Task 2 ##########")
    BST2 = BinarySearchTree()
    #            12
    #       4         20
    #     1   8    16   27
    random_data = [12, 4, 20, 8, 1, 16, 27]
    for data in random_data:
        BST2.insert(data)

    print()
    print("Testing Pre-order Traversal...")
    traversed_data = []
    BST2.traverse_pre_order(BST2.root, traversed_data)
    assert(traversed_data == [12, 4, 1, 8, 20, 16, 27])
    print("PASSED!")

    print()
    print("Testing Post-order Traversal...")
    traversed_data = []
    BST2.traverse_post_order(BST2.root, traversed_data)
    assert(traversed_data == [1, 8, 4, 16, 27, 20, 12])
    print("PASSED!")
