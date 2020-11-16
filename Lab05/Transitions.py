class Transitions:
    def __init__(self):
        self.dictionary = {}

    def __str__(self):
        result = ""
        for start in self.dictionary.keys():
            for transition in self.dictionary[start]:
                aux = start + " --> " + transition[1] + " --> " + transition[0] + "\n"
                result += aux
        return result

    def addTransition(self, start, end, value):
        '''
        :param start: starting position dictionary
        :param end: end position in dictionary
        :param value: as the name implies represents the value to be added
        :return: adds a new Transition to our transitions dictionary
        '''
        if start in self.dictionary.keys():
            self.dictionary[start].append((end, value))
        else:
            self.dictionary[start] = [(end, value)]

    def getTransitionsWithStart(self, start):
        '''
        :param start: position of the start
        :return: our dictionary from the given start
        '''
        if start not in self.dictionary.keys():
            return []
        return self.dictionary[start]
