from operator import index
import random
import string
from utils.logger import get_logger

from genetic.chromosome import Chromosome
from .genotype import Genotype_TSP

class Chromosome_TSP(Chromosome):
    r"""Chromosome class for TSP example"""
    logger = None

    def __init__(self, genotypes, fitness_score=0.0):
        super().__init__(genotypes, fitness_score)
        self.total_distance = None

        self.logger = get_logger()

    def crossover(self, partner):
        r"""Performs crossover between two chromosomes"""
        self.logger.debug("Performing crossover for chromosome")
        chromosome_child = None

        # get random half from self and the other half from partner
        midpoint = random.randint(0, self._chromosome_size)

        genotypes = self._genotypes[0: midpoint] + partner._genotypes[midpoint: self._chromosome_size]
        chromosome_child = Chromosome_TSP(genotypes)

        return chromosome_child

    def mutate(self, mutation_rate):
        r"""Performs mutation based on mutation rate"""
        self.logger.debug(f"Performing mutation at a rate {mutation_rate}")

        # pick a uniform random number and mutate if its before the mutation rate
        if random.uniform(0, 1) < mutation_rate:
            # swap two indices except the starting index
            
            possibilities = [i for i in range(1, len(self._genotypes))]
            indices = random.sample(possibilities, k=2)

            t = self._genotypes[indices[0]]
            self._genotypes[indices[0]] = self._genotypes[indices[1]]
            self._genotypes[indices[1]] = t

    def calculate_fitness_score(self, fitness_fn):
        f"""Calculates the fitness score of this Chromosome based on the fitness function"""

        index_order = []
        for geno in self._genotypes:
            index_order.append(geno.get_value())

        total_distance, fitness_score = fitness_fn(index_order=index_order)

        self.fitness_score = fitness_score
        self.total_distance = total_distance

    def __str__(self):
        r"""String representation"""
        return ("Chromosome_TSP(Chromosome) \n"
                "\tgenotypes = {0}, \n"
                "\ttotal distance = {1}, \n"
                "\tfitness_score = {2}, \n"
                "\tnormalized_fitness_score = {3}".format(self._short_repr(), self.total_distance, self.fitness_score, self.normalized_fitness_score))

    def _short_repr(self):
        r"""Short representation of the chromosome"""
        decoded_string = "Travel order: "

        decoded_string += self._genotypes[0].decoded_value
        for geno in self._genotypes[1:]:
            decoded_string += " -> " + geno.decoded_value

        return decoded_string