import Node


class NodeOperations:
    @staticmethod
    def search(root: Node, identifier):
        if root is None:
            return None
        if root.identifier == identifier:
            return root
        if root.identifier > identifier:
            return NodeOperations.search(root.left, identifier)
        if root.identifier < identifier:
            return NodeOperations.search(root.right, identifier)
        return None

    @staticmethod
    def insert(root: Node, node: Node):
        if root is None:
            root = node
        else:
            if root.identifier < node.identifier:
                if root.right is None:
                    root.right = node
                else:
                    NodeOperations.insert(root.right, node)
            else:
                if root.left is None:
                    root.left = node
                else:
                    NodeOperations.insert(root.left, node)

    @staticmethod
    def inOrder(root: Node):
        if root:
            NodeOperations.inOrder(root.left)
            print("#" + root.identifier + "=>" + str(root.position))
            NodeOperations.inOrder(root.right)
