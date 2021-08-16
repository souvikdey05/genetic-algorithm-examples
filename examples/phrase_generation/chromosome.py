from typing import Any, List

from genetic.chromosome import Chromosome

class Chromosome_PhraseGeneration(Chromosome):
    r"""Chromosome class for phrase generation example"""

    def __init__(self, genotypes):
        super().__init__(genotypes)

    def crossover(self, partner):
        r"""Performs crossover between two chromosomes"""
        print("crossover")

        return None

    def mutate(self, mutation_rate):
        r"""Performs mutation based on mutation rate"""
        print("mutation")
        return None

    def calculate_fitness_score(self, fitness):
        f"""Calculates the fitness score of this Chromosome based"""
        print("calculate_fitness_score")

        return 0.0