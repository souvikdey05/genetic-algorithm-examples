from typing import List

from genetic.population import Population

class Population_PhraseGeneration(Population):
    r"""Population class for phrase generation example"""

    def __init__(self, chromosomes,  mutation_rate):
        super().__init__(chromosomes, mutation_rate)

        self._chromosomes = chromosomes
        self._generations = 0
        self._mutation_rate = mutation_rate

    def run(self):
        r"""Implementation of run method"""
        print("Perform run")