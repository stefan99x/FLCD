from Lab04.FiniteAutomata import *


def printMenu():
    '''
    Prints the Menu
    :return:
    '''
    print("{1}. Print States")
    print("{2}. Print Alphabet")
    print("{3}. Print Initial State")
    print("{4}. Print Transitions")


if __name__ == '__main__':
    finiteAutomata = FiniteAutomatan("fa.in")
    options = {1: finiteAutomata.printStates(), 2: finiteAutomata.printAlphabet(),
               3: finiteAutomata.printInitialState(), 4: finiteAutomata.printTransitions()}
    while True:
        printMenu()
        try:
            opt = int(input(">>"))
            if opt not in range(1, 5):
                pass
            options[opt]()
            print()
        except Exception as ex:
            print(ex)
            pass
