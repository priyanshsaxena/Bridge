import numpy as np

import abc
class deck(metaclass=abc.ABCMeta):
    def __init__(self):
        self.arr = np.arange(1,53,1)
    
    def Shuffle(self):
        arr =self.arr
        np.random.shuffle(arr)
        self.arr = arr

    def Method1111(self):
        divisions = [[],[],[],[]]
        for i in range (52):
            divisions[i%4].append(self.arr[i])
        return divisions
    
    def Method1313(self):
        divisions = [[],[],[],[]]
        for i in range (52):
            divisions[int(i//13)].append(self.arr[i])
        return divisions
    
    def Method544(self):
        divisions = [[],[],[],[]]
        for i in range (20):
            divisions[i//5].append(self.arr[i])
        for i in range (20,36):
            divisions[(i-20)//4].append(self.arr[i])
        for i in range (36,52):
            divisions[(i-36)//4].append(self.arr[i])
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
print(deck1.Method1313())
print(deck1.Method544())


