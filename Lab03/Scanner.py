from Lab03.Token import *
from Lab03.SymbolTable import SymbolTable
from Lab03.PIF import PIF
import re


class Scanner:
    def __init__(self, file):
        self.SymbolTable = SymbolTable()
        self.filename = file
        self._tokens = getTokens()
        self.PIF = PIF()

    @staticmethod
    def isConstant(token):
        isConstant = re.match("^0$|^(([+\\-])?[1-9][0-9]*)$", token)
        isBool = token == "true" or token == "false"
        isString = re.match("^\"([a-zA-Z0-9_.?,!; @/|(){}\[\]\+\-*%$])*\"$", token)

        return isConstant or isBool or isString

    @staticmethod
    def isOperator(token):
        return token in operators

    @staticmethod
    def isIdentifier(token):
        return re.match('^[a-zA-Z_]([a-zA-Z0-9]){,255}$', token) is not None

    @staticmethod
    def getStringConstant(line, index):
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
                token, index = Scanner.getStringConstant(line, index)
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
                if operator is not None:
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
            isOk = True
            for line in file:
                tokens = Scanner.getTokensFromLine(line)
                print(tokens)
                for token in tokens:
                    if token in separators or token in operators or token in reservedWords:
                        self.PIF.add(self._tokens[token], -1)

                    elif Scanner.isIdentifier(token):
                        id = self.SymbolTable.insert(token)
                        self.PIF.add(self._tokens['identifier'], id)

                    elif Scanner.isConstant(token):
                        id = self.SymbolTable.insert(token)
                        self.PIF.add(self._tokens['constant'], id)

                    else:
                        # raise Exception("Invalid token " + token + " at the line" + str(lineNumber))
                        print("Invalid Token: { " + token + " } at line: " + str(lineNumber) + "\n")
                        isOk = False

                lineNumber += 1

            if isOk:
                print("All good homie")
                print(self.PIF)
                self.PIF.printToFile()

                self.SymbolTable.print()
                self.SymbolTable.printToFile()
            else:
                print("Lexically incorrect. ")

            print(self.PIF)
            print(self.SymbolTable.print())
