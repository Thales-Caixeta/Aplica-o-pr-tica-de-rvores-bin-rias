class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert(current_node.left, value)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert(current_node.right, value)

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.value, end=' ')
            self.inorder_traversal(node.right)

    def preorder_traversal(self, node):
        if node:
            print(node.value, end=' ')
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    def postorder_traversal(self, node):
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.value, end=' ')

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, current_node, value):
        if current_node is None or current_node.value == value:
            return current_node
        if value < current_node.value:
            return self._search(current_node.left, value)
        return self._search(current_node.right, value)

# Exemplo de uso:
if __name__ == "__main__":
    tree = BinaryTree()
    nodes = [50, 30, 20, 40, 70, 60, 80]

    for node in nodes:
        tree.insert(node)

    print("In-order traversal:")
    tree.inorder_traversal(tree.root)
    print("\nPre-order traversal:")
    tree.preorder_traversal(tree.root)
    print("\nPost-order traversal:")
    tree.postorder_traversal(tree.root)

    print("\nBusca por valor 80:")
    found_node = tree.search(90)
    if found_node:
        print(f"Valor {found_node.value} encontrado!")
    else:
        print("Valor não encontrado.")
