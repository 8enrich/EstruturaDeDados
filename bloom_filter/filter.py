import mmh3
from random import sample

class Lista(list):

    def __init__(self, size=0, hash_functions_quantity=0):
        self.__bit_array = [0] * size
        self.__size = size
        self.__hash_functions_quantity = hash_functions_quantity
        self.__seeds = sample(range(1, 10000000), hash_functions_quantity)

    def indexes(self, value):
        indexes = map(lambda x: mmh3.hash(value, seed=self.__seeds[x], signed=False)%self.__size, range(self.__hash_functions_quantity))
        return indexes

    def add(self, value):
        for i in self.indexes(value):
            self.__bit_array[i] = 1

    def __contains__(self, key):
        for i in self.indexes(key):
            if self.__bit_array[i] != 1:
                return False
        return True
