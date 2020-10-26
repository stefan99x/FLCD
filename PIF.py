class PIF:
    def __init__(self):
        self.pif = []

    def add(self, code, position):
        self.pif.append((code, position))

    def __str__(self):
        text = "PIF: \n"
        for element in self.pif:
            text += str(element[0]) + " -> " + str(element[1]) + "\n"
        return text
