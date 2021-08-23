import random
import string
from utils.logger import get_logger

from genetic.population import Population

from .chromosome import Chromosome_PhraseGeneration
from .genotype import Genotype_PhraseGeneration
from .fitness import Fitness_PhraseGeneration

class Population_PhraseGeneration(Population):
    r"""Population class for phrase generation example"""
    logger = None

    def __init__(self, population_size,  mutation_rate, target_phrase, max_generations=None):
        super().__init__(population_size, mutation_rate)
        self._target_phrase = target_phrase  # the target phrase
        self._max_generations = max_generations # The max number of generations to run
        self._fitness = Fitness_PhraseGeneration(target_phrase)  # the fitness object
        self._eps = 0.001  # a small value to give some probability to fitness of each chromosome incase the fitness is zero
        self._solution_found = False    # flag to indicate solution is found

        self.logger = get_logger()

        self._generate_initial_population()
    
    def _generate_initial_population(self):
        r"""method to generate the initial population"""
        self.logger.info("Generating first population")

        string.ascii_letters = "abcdefghijklmnopqrstuvwxyz"  # Only lower case letters for now
        # generate multiple chromosomes for a population
        self._chromosomes = []
        for p in range(self._population_size):

            # generate genotype for each chromosome
            # the length of the target phrase gives the number of genotype for a chromosome
            genotypes = []
            for i in range(len(self._target_phrase)):
                geno = Genotype_PhraseGeneration(random.choice(string.ascii_letters))
                genotypes.append(geno)
            
            chromo = Chromosome_PhraseGeneration(genotypes)
            self._chromosomes.append(chromo)

        self._increment_generation()
    
    def _refill_population(self):
        r"""Method to refill the new population using crossover and mutation"""
        chromosomes = []
        
        for p in range(self._population_size):
            chromosome_parent_A = self._natural_selection()
            chromosome_parent_B = self._natural_selection()
            chromosome_child = chromosome_parent_A.crossover(chromosome_parent_B)
            chromosome_child.mutate(self._mutation_rate)
            chromosomes.append(chromosome_child)

        self._chromosomes = chromosomes     # new population

        self._increment_generation()

    def _increment_generation(self):
        r"""Method to increment generation count"""
        self._generations = self._generations + 1


    def _calculate_fitness(self):
        r"""Calculate the fitness of each chromosome in the population"""
        sum = 0.0
        best_fitness_score = 0.0
        best_chromosome = None
        for chromo in self._chromosomes:
            chromo.calculate_fitness_score(self._fitness.fitness)
            if chromo.fitness_score > best_fitness_score:
                best_fitness_score = chromo.fitness_score
                best_chromosome = chromo

            sum = sum + chromo.fitness_score

        self._avg_fitness_score = sum / self._population_size
        self._best_fitness_score = best_fitness_score
        self._best_chromosome = best_chromosome

        # Normalize to a probability value   
        for chromo in self._chromosomes:
            chromo.normalized_fitness_score = (chromo.fitness_score / sum ) + self._eps

    def _natural_selection(self):
        r"""select parent (i.e. chromosome) according to accept-reject sampling strategy"""
        
        besafe = 0  # variable to keep the infinite loop in check

        while True:
            index = random.randint(0, self._population_size - 1)
            selected_chromo = self._chromosomes[index]

            random_acceptance = random.uniform(0, 1)
            if random_acceptance < selected_chromo.normalized_fitness_score:
                return selected_chromo

            besafe = besafe + 1
            if besafe > 10000:
                return None

    
    def run(self):
        r"""Implementation of run method"""
        self.logger.info("Perform run")

        while not self._solution_found:
            self.logger.info(f"Generation = {self._generations}")
            # calculate the fitness of each chromosome
            self.logger.info("Calculating fitness score ->")
            self._calculate_fitness()
            
            self.logger.info(f"Best Chromosome = {self._best_chromosome}")
            self.logger.info(f"Best fitness score = {self._best_fitness_score}")

            self._refill_population()

            # if the solution is found
            if self._best_fitness_score == len(self._target_phrase):
                self.logger.info("Solution found")
                self._solution_found = True

            # if there is a constraint for max generations
            if self._max_generations is not None and self._generations >= self._max_generations:
                break

        if self._solution_found:
            self.logger.info(f"Solution: {self._best_chromosome}")
            self.logger.info(f"Generation #: {self._generations}")

        else:
            self.logger.info("Solution not found")