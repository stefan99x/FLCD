from SymbolTable import *

if __name__ == "__main__":
    symbolTable = SymbolTable()

    symbolTable.insert("stefan")
    symbolTable.insert("nota5")
    symbolTable.insert("primeste")
    symbolTable.insert("stefan")
    symbolTable.insert("stefan")

    print(symbolTable.insert("cevaDiferit"))
    print(symbolTable.insert("primeste"))

    symbolTable.print()
