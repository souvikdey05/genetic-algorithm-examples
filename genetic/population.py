from typing import List
from abc import ABC, abstractmethod
from typing import List

class Population(ABC):
    r""" The Base Population class
    """
    def __init__(self, population_size, mutation_rate):
        self._chromosomes = None                # list of chromosomes in the current population
        self._population_size = population_size # the population size
        self._generations = 0                   # generation number
        self._mutation_rate = mutation_rate     # mutation rate
        self._avg_fitness_score = 0.0           # avg fitness score of the population
        self._best_fitness_score = 0.0          # best fitness score of the population
        self._best_chromosome = None            # best chromosome of the population based on highest fitness score

    @abstractmethod
    def _generate_initial_population(self):
        r"""generates the initial population"""
        pass
    
    @abstractmethod
    def run(self):
        r"""Runs over all the chromosomes to calculate fitness,
        natural selection and generate new population"""
        pass
