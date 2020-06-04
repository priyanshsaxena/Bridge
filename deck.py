import numpy as np

import abc
class deck(metaclass=abc.ABCMeta):
    def __init__(self):
        self.arr = np.arange(1,53,1)
    def Shuffle(self):
        arr =self.arr
        np.random.shuffle(arr)
        self.arr = arr
    def get_shuffled_deck(self):
        arr = self.arr
        return arr

    def Method1111(self):
        divisions = [[],[],[],[]]
        for i in range (52):
            divisions[i%4].append(self.arr[i])
        return divisions
    
    def Method1313(self):
        divisions = [[],[],[],[]]
        for i in range (52):
            p[i%4].append(self.arr[i])
        return divisions
    
    def Method544(self):
        divisions = [[],[],[],[]]
        for i in range (52):
            p[i%4].append(self.arr[i])
        return divisions

    @abc.abstractmethod
    def func(self):
        pass


class Deck(deck):
    def func(self):
        pass


deck1 = Deck()
deck1.Shuffle()
print(deck1.Method1111())


