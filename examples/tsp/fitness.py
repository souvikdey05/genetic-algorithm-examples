from genetic.fitness import Fitness


class Fitness_TSP(Fitness):
    r"""Fitness class for TSP example"""

    def __init__(self):
        super().__init__()

    def fitness(self, phrase):
        # Method to calculate fitness
        # Here the fitness is the number of characters that matches
        # Here the fitness is the number of characters that matches normalized by length of the phrase
        fitness_value = 0.0
        for i, c in enumerate(phrase):
            if c == self._target[i]:
                fitness_value = fitness_value + 1

        # fitness_value = fitness_value / len(phrase)
        return fitness_value