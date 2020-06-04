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

    @abc.abstractmethod
    def divide_cards(self):
        pass

class Method1111(deck):
    def divide_cards(self):
        p = [[],[],[],[]]
        for i in range (52):
            p[i%4].append(self.arr[i])
        return p

deck1 = Method1111()
deck1.Shuffle()
print(deck1.divide_cards())

