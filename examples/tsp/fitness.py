#from genetic.fitness import Fitness
from scipy.spatial import distance

class Fitness_TSP():
    r"""Fitness class for TSP example"""

    def __init__(self):
        super().__init__()
        self._eps = 0.001   # a small number 0.001 to avoid division by 0

    def fitness(self, coordinates, index_order):
        # Method to calculate fitness
        fitness_value = 0.0
        
        total_distance = 0
        # calculate the euclidean distance in order of the coordinates visited
        for i in range(len(index_order)-1):
            total_distance = distance.euclidean(coordinates[index_order[i]], coordinates[index_order[i+1]])

        # fitness value is the inverse of total distance. Smaller the distance, better is the fitness
        # adding a small number 0.001 to avoid division by 0
        fitness_value = 1 / (total_distance + + self._eps)

        return total_distance, fitness_value