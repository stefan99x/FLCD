from BinarySearchTree import BinarySearchTree


class SymbolTable:
    def __init__(self):
        self.tree = BinarySearchTree()

    def insert(self, identifier):
        return self.tree.insert(identifier)

    def print(self):
        self.tree.printBinarySearchTree()

    def printToFile(self):
        self.tree.printToFile()
