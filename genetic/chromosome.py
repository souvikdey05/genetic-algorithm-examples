from abc import ABC, abstractmethod

class Chromosome(ABC):
    r""" The Base Chromosome class     
    """
    def __init__(self, genotypes):
        self._genotypes = genotypes
        self.fitness_score = 0.0

    @abstractmethod
    def crossover(self, partner):
        r"""Performs crossover between two chromosomes"""
        pass

    @abstractmethod
    def mutate(self, mutation_rate):
        r"""Performs mutation based on mutation rate"""
        pass

    @abstractmethod
    def calculate_fitness_score(self, fitness):
        f"""Calculates the fitness score of this Chromosome based
        on the fitness type"""
        pass