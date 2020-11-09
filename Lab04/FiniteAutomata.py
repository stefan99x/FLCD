
from Lab04.Transitions import Transitions


class FiniteAutomatan:
    def __init__(self, fileName):
        self.delta = Transitions()
        self.fileName = fileName
        self.Q = set()  # States
        self.E = set()  # Alphabet
        self.F = set()  # Transitions
        self.Q0 = None  # Initial State
        self.readFromFile()

    def readFromFile(self):
        '''
        as the name implies reads from a given file
        '''
        with open(self.fileName, 'r') as file:

            self.Q = file.readline().strip('\n').split(' ')
            self.E = file.readline().strip('\n').split(' ')
            self.F = file.readline().strip('\n').split(' ')
            self.Q0 = file.readline().strip('\n').split(' ')
            line = file.readline().strip('\n')

            while line:

                line = line.split(' ')
                for index in range(2, len(line)):
                    self.delta.addTransition(line[0], line[1], line[index])
                line = file.readline().strip('\n')

    def printStates(self):
        '''
        Print all the States
        '''
        print("States")
        for state in self.Q:
            print(state)

    def printAlphabet(self):
        '''
        Print all the Alphabet
        '''
        print("Alphabet of FA:")
        for value in self.E:
            print(value)

    def printInitialState(self):
        '''
        Print the initial State
        '''
        print(f"Initial state of FA: {self.Q0}")

    def printTransitions(self):
        '''
        Print the transitions
        '''
        print(f"Transitions: {self.delta}")

    def isDeterministic(self):
        '''
        Checks if it is deterministic
        :return: true or false
        '''
        for state in self.Q:
            transitions = self.delta.getTransitionsWithStart(state)
            for transition in transitions:
                uniqueTransitions = list(filter(lambda x: x[1] != transition[1], transitions))
                if len(uniqueTransitions) != len(transitions) - 1:
                    return False
        return True

    def isAccepted(self, string):
        '''
        Checks if it is accepted a given string
        :param string: input string
        :return: true or false
        '''
        if not self.isDeterministic():
            raise Exception("Not deterministic, sorry fam, quite sad init")
        currentState = self.Q0

        for index in range(len(string)):
            possibleTransitions = self.delta.getTransitionsWithStart(currentState)
            currentValue = string[index]
            currentState = None

            for transition in possibleTransitions:
                if transition[1] == currentValue:
                    currentState = transition[0]

            if currentState is None:
                return False

        if currentState not in self.F:
            return False

        return True
