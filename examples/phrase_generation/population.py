from genetic.population import Population
from .fitness import Fitness_PhraseGeneration

class Population_PhraseGeneration(Population):
    r"""Population class for phrase generation example"""

    def __init__(self, chromosomes,  mutation_rate, target_phrase):
        super().__init__(chromosomes, mutation_rate)
        self._target_phrase = target_phrase  # the target phrase
        self._fitness = Fitness_PhraseGeneration(target_phrase)  # the fitness object
        self._eps = 0.001  # a small value to give some probability to fitness of each chromosome incase the fitness is zero

    def _calculate_fitness(self):
        # Calculate the fitness of each chromosome in the population
        sum = 0.0
        for chromo in self.chromosomes:
            chromo._calculate_fitness_score(self._fitness.fitness)
            sum = sum + chromo.fitness_score

        # Normalize to a probability value   
        for chromo in self.chromosomes:
            chromo.fitness_score = (chromo.fitness_score / sum ) + self._eps 
    
    def run(self):
        r"""Implementation of run method"""
        print("Perform run")