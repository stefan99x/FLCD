from Node import Node
from NodeOperations import NodeOperations


class BinarySearchTree:
    def __init__(self):
        self.currentPosition = 1
        self.root = None

    def printBinarySearchTree(self):
        NodeOperations.inOrder(self.root)

    def search(self, identifier):
        return NodeOperations.search(self.root, identifier)

    def insert(self, identifier):
        newNode = Node(identifier)
        if self.root is None:
            self.root = newNode
            newNode.position = self.currentPosition
            self.currentPosition += 1

        node = self.search(identifier)
        if node:
            return node.position

        NodeOperations.insert(self.root, newNode)
        newNode.position = self.currentPosition
        self.currentPosition += 1

    def printToFile(self):
        NodeOperations.printToFile(self.root)
