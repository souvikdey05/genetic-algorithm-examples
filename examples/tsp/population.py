import random
from utils.logger import get_logger
import csv
from functools import partial
from genetic.population import Population
from tqdm import tqdm
from math import inf

from .chromosome import Chromosome_TSP
from .genotype import Genotype_TSP
from .fitness import Fitness_TSP

class Population_TSP(Population):
    r"""Population class for TSP example"""
    logger = None

    def __init__(self, coordinates, starting_index, population_size,  mutation_rate):
        super().__init__(population_size, mutation_rate)
        self._coordinates = coordinates
        self._starting_index = starting_index

        self._fitness = Fitness_TSP()  # the fitness object
        self._eps = 0.001  # a small value to give some probability to fitness of each chromosome incase the fitness is zero

        self.logger = get_logger()

        self._generate_initial_population()
    
    def _generate_initial_population(self):
        r"""method to generate the initial population"""
        self.logger.info("Generating first population")
        
        # generate multiple chromosomes for a population
        self._chromosomes = []

        # all the indices of the coordinate list are possibilities except the starting index
        possibilities = [i for i in range(len(self._coordinates))]
        possibilities.pop(self._starting_index)

        combinations = []

        for _ in range(self._population_size):
            # generate genotype for each chromosome
            genotypes = []

            # the starting coordinate will not change
            geno = Genotype_TSP(self._starting_index)
            genotypes.append(geno)

            one_genotype_simple = [self._starting_index]

            new_possibility = random.sample(possibilities, k=len(possibilities))
            
            re_tries = 10
            # if there are duplicate random combinations then find another one
            while one_genotype_simple + new_possibility in combinations and re_tries > 0:
                new_possibility = random.sample(possibilities, k=len(possibilities))
                re_tries -= 1

            if re_tries == 0:
                raise Exception("Not able to find unique initial population")
                
            one_genotype_simple = one_genotype_simple + new_possibility

            for i in new_possibility:
                geno = Genotype_TSP(i)
                genotypes.append(geno)
            
            chromo = Chromosome_TSP(genotypes)
            self._chromosomes.append(chromo)
            combinations.append(one_genotype_simple)
    
    def refill_population(self):
        r"""Method to refill the new population using crossover and mutation"""
        chromosomes = []
        
        for p in range(self._population_size):
            chromosome_parent_A = self._natural_selection()
            chromosome_parent_B = self._natural_selection()
            chromosome_child = chromosome_parent_A.crossover(chromosome_parent_B)
            # chromosome_child = chromosome_parent_A.crossover_v2(chromosome_parent_B, self._target_phrase)
            # chromosome_child = self._natural_selection()

            if self._mutation_rate > 0:
                chromosome_child.mutate(self._mutation_rate)
            chromosomes.append(chromosome_child)

        self._chromosomes = chromosomes     # new population

    def calculate_fitness(self):
        r"""Calculate the fitness of each chromosome in the population"""
        sum = 0.0
        best_generation_distance = inf
        best_generation_fitness_score = 0.0
        best_generation_chromosome = None

        fitness_function = partial(self._fitness.fitness, coordinates=self._coordinates)
        for chromo in self._chromosomes:
            chromo.calculate_fitness_score(fitness_function)
            if chromo.total_distance is not None and chromo.total_distance < best_generation_distance:
                best_generation_distance = chromo.total_distance
                best_generation_fitness_score = chromo.fitness_score
                best_generation_chromosome = chromo

            sum = sum + chromo.fitness_score

        self._avg_fitness_score = sum / self._population_size
        self._best_generation_distance = best_generation_distance
        self._best_generation_fitness_score = best_generation_fitness_score
        self._best_generation_chromosome = best_generation_chromosome

        # Normalize to a probability value   
        for chromo in self._chromosomes:
            chromo.normalized_fitness_score = (chromo.fitness_score / sum ) + self._eps

            self.logger.info(f"chromosome = {chromo}")

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

    def _write_scores(self, scores):
        r"""Method to write the generation number and scores in a file"""
        if self._score_file is not None:
            with open(self._score_file, "w", newline='') as file:
                writer = csv.writer(file)

                # write the header
                writer.writerow(['Generation', 'Best Fitness Score', 'Best Chromosome'])

                for s in scores:
                    writer.writerow(s)

    def run(self):
        r"""Implementation of run method"""
        pass