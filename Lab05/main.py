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
    print("{5}. Check if it is Deterministic")
    print("{6}. Check if it is Accepted")


def isDeterministic():
    result = finiteAutomata.isDeterministic()
    if result:
        print("Is deterministic")
    else:
        print("A bit sad init homie")


def isAccepted():
    text = input("Enter your word:")
    result = finiteAutomata.isAccepted(text)
    if result:
        print("Word: " + text + "is accepted :)")
    else:
        print("Word: " + text + "is not accepted :(")


if __name__ == '__main__':
    # nonDeterministic.in
    #finiteAutomata = FiniteAutomatan("nonDeterministic.in")
    finiteAutomata = FiniteAutomatan("fa.in")
    options = {1: finiteAutomata.printStates, 2: finiteAutomata.printAlphabet,
               3: finiteAutomata.printInitialState, 4: finiteAutomata.printTransitions,
               5: isDeterministic, 6: isAccepted}
    while True:
        printMenu()
        try:
            opt = int(input(">>"))
            if opt not in range(1, 7):
                pass
            options[opt]()
            print()
        except Exception as ex:
            print(ex)
            pass
