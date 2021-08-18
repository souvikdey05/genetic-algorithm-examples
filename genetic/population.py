from typing import List
from abc import ABC, abstractmethod
from typing import List

class Population(ABC):
    r""" The Base Population class
    """
    def __init__(self, chromosomes, mutation_rate):
        self._chromosomes = chromosomes     # list of chromosomes in the current population
        self._generations = 0               # generation number
        self._mutation_rate = mutation_rate # mutation rate

    @abstractmethod
    def run(self):
        r"""Runs over all the chromosomes to calculate fitness,
        natural selection and generate new population"""
        pass
