class NumSum:

    def __init__(self, n1, n2):
        self.num1 = 0
        self.num2 = 0
        self.setN1N2(n1, n2)

    def setN1N2(self, n1, n2):
        self.num1 = n1
        self.num2 = n2

        if n1 < n2:
            self.num1 = n2
            self.num2 = n1

    def addNum(self, n):
        if n <= 1:
            return n

        return n + self.addNum(n-1)

    def sumBetweenNums(self):
        return self.addNum(self.num1 - 1) - self.addNum(self.num2)
