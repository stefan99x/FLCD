from Token import *
from SymbolTable import SymbolTable
from PIF import PIF
import re


class Scanner:
    def __init__(self, file):
        self.SymbolTable = SymbolTable()
        self.filename = file
        self._tokens = getTokens()
        self.PIF = PIF()

    @staticmethod
    def isConstant(token):
        return re.match('^[a-zA-Z_]([a-zA-Z0-9]){,255}$', token) is not None

    @staticmethod
    def isOperator(token):
        return token in operators

    @staticmethod
    def isIdentifier(token):
        return re.match('^[a-zA-Z_]([a-zA-Z0-9]){,255}$', token) is not None

    @staticmethod
    def getString(line, index):
        token = ''
        numberOfQuotes = 0
        while index < len(line) and numberOfQuotes < 2:
            if (line[index] == '"'):
                numberOfQuotes += 1
            token += line[index]
            index += 1
        return token, index

    @staticmethod
    def getOperator(line, index):
        i = index
        token = ""
        while i < len(line) and line[i] not in operators and Scanner.isContainedInOperator(line[i]):
            token += line[i]
            i += 1
        if token in operators:
            return token, i
        return None, index

    @staticmethod
    def isContainedInOperator(token):
        for operator in operators:
            if token in operator:
                return True
        return False

    @staticmethod
    def getWholeOperator(line, index):
        token = ''
        while index < len(line) and Scanner.isOperator(line[index]):
            token += line[index]
            index += 1
        return token, index

    @staticmethod
    def getTokensFromLine(line):
        token = ''
        index = 0
        tokens = []

        while index < len(line):
            if line[index] == '"':
                if token:
                    tokens.append(token)
                token, index = Scanner.getString(line, index)
                tokens.append(token)
                token = ""

            elif line[index] in separators:
                if token:
                    tokens.append(token)
                token = ""
                tokens.append(line[index])
                index += 1

            elif Scanner.isContainedInOperator(line[index]):
                operator, index = Scanner.getOperator(line, index)
                if operator != None:
                    if token:
                        tokens.append(token)
                    tokens.append(operator)
                    token = ""
                else:
                    token += line[index]
                    index += 1

            else:
                token += line[index]
                index += 1

            if token:
                tokens.append(token)

            return tokens

    def run(self):
        with open(self.filename, "r") as file:
            lineNumber = 1
            for line in file:
                tokens = Scanner.getTokensFromLine(line)
                print(tokens)
                for token in tokens:
                    if token in separators or token in operators or token in reservedWords:
                        self.PIF.add(self._tokens[token], 1)

                    elif Scanner.isIdentifier(token):
                        id = self.SymbolTable.insert(token)
                        self.PIF.add(self._tokens['identifier'], id)

                    elif Scanner.isConstant(token):
                        id = self.SymbolTable.insert(token)
                        self.PIF.add(self._tokens['constant'], id)

                    else:
                        raise Exception("Invalid token " + token + " at the line" + str(lineNumber))

                lineNumber += 1

            print(self.PIF)
            print(self.SymbolTable.print())