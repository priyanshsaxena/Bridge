import abc

import numpy as np


class deck(metaclass=abc.ABCMeta):
    def __init__(self):
        self.arr = np.arange(1, 53, 1)

    @abc.abstractmethod
    def Shuffle(self):
        pass

    def Distribute(self):
        pass


class Deck(deck):
    def Shuffle(self):
        arr = self.arr
        np.random.shuffle(arr)
        self.arr = arr

    def Distribute(self, distributeMethod):
        divisions = [[], [], [], []]
        if distributeMethod == "1111":
            for i in range(52):
                divisions[i % 4].append(self.arr[i])
            return divisions

        elif distributeMethod == "1313":
            for i in range(52):
                divisions[int(i//13)].append(self.arr[i])
            return divisions
        elif distributeMethod == "544":
            for i in range(20):
                divisions[i//5].append(self.arr[i])
            for i in range(20, 36):
                divisions[(i-20)//4].append(self.arr[i])
            for i in range(36, 52):
                divisions[(i-36)//4].append(self.arr[i])
            return divisions


deck1 = Deck()
deck1.Shuffle()
print(deck1.Distribute("1111"))
print(deck1.Distribute("1313"))
print(deck1.Distribute("544"))
