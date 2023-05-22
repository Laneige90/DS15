class MinAlgorithm:

    def __init__(self,cs):
        self.chars = cs
        self.minChar = 0

    def getMiniChar(self):
        self.minChar = self.chars[0]

        for c in self.chars:
            if ord(self.minChar) > ord(c):
                self.minChar = c

        return self.minChar

ma = MinAlgorithm(['c', 'x', 'Q', 'A', 'e', 'p', 'P'])
minChar = ma.getMiniChar()
print(minChar)