codes = {
    "identifier": 0,
    "constant": 1,
    " ": 2,
    "+": 3,
    "-": 4,
    "*": 5,
    "/": 6,
    "%": 7,
    "=": 8,
    "==": 9,
    "!=": 11,
    "<=": 12,
    ">=": 13,
    ">": 14,
    "<": 15,
    "#": 16,
    "tni": 17,
    "loob": 18,
    "gnirts": 19,
    "rahc": 20,
    "pool": 21,
    "fi": 22,
    "esle": 23,
    "elihw": 24,
    "noitcnuf": 25,
    "daer": 26,
    "etirw": 27,
    "true": 28,
    "false": 29,
    ":": 30,
    ";": 31,
    "(": 32,
    ")": 33,
    "{": 34,
    "}": 35,
    "[": 36,
    "]": 37,
    "&": 38,
    "|": 39,

}

operators = ['+', '-', '*', '/', '=', '<', '<=', '>', '>=', '&', '|']

reservedWords = ["loob", "gnirts", "rahc", "pool", "fi", "esle", "elihw", "noitcnuf", "daer", "etirw", "true", "false"]

separators = [')', '(', ']', '[', '}', '{', ';', ':']


def getTokens():
    tokens = {}
    currentId = 0
    with open("tokens.in", 'r') as file:
        for line in file:
            line = line.strip("\n")
            token = line
            if token == "":
                token = " "
            tokens[token] = currentId
            currentId += 1
        tokens['\n'] = currentId
    return tokens
