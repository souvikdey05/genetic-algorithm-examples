import random
import string
from utils.logger import get_logger

from genetic.chromosome import Chromosome
from .genotype import Genotype_PhraseGeneration

class Chromosome_PhraseGeneration(Chromosome):
    r"""Chromosome class for phrase generation example"""
    logger = None

    def __init__(self, genotypes, fitness_score=0.0):
        super().__init__(genotypes, fitness_score)
        self.logger = get_logger()

    def crossover(self, partner):
        r"""Performs crossover between two chromosomes"""
        self.logger.debug("Performing crossover for chromosome")
        chromosome_child = None

        # get random half from self and the other half from partner
        midpoint = random.randint(0, self._chromosome_size)

        genotypes = self._genotypes[0: midpoint] + partner._genotypes[midpoint: self._chromosome_size]
        chromosome_child = Chromosome_PhraseGeneration(genotypes)

        return chromosome_child

    def crossover_v2(self, partner, target):
        r"""Performs crossover between two chromosomes.
            Strategy: copy the gene which have the correct values from both the parents. The remaining gene are filled with random values"""
        self.logger.debug("Performing crossover for chromosome")
        chromosome_child = None

        genotypes = ['Junk' for _ in range(self._chromosome_size)] ## creating a placeholder for gene with all junk
        for i in range(self._chromosome_size):
            if self._genotypes[i].decoded_value == target[i]:
                geno = self._genotypes[i]
            elif partner._genotypes[i].decoded_value == target[i]:
                geno = partner._genotypes[i]
            else:
                ## fill with some random character
                string.ascii_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ,.'"
                geno = Genotype_PhraseGeneration(random.choice(string.ascii_letters))
            genotypes[i] = geno

        chromosome_child = Chromosome_PhraseGeneration(genotypes)

        return chromosome_child

    def mutate(self, mutation_rate):
        r"""Performs mutation based on mutation rate"""
        self.logger.debug(f"Performing mutation at a rate {mutation_rate}")

        string.ascii_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ,.'"

        # pick a unifirm random number and mutate if its before the mutation rate
        for i in range(self._chromosome_size):
            if random.uniform(0, 1) < mutation_rate:
                # pick another random char and change it
                self._genotypes[i] = Genotype_PhraseGeneration(random.choice(string.ascii_letters))

    def calculate_fitness_score(self, fitness_fn):
        f"""Calculates the fitness score of this Chromosome based on the fitness function"""

        decoded_string = ""
        for geno in self._genotypes:
            decoded_string += geno.decoded_value

        fitness_score = fitness_fn(decoded_string)
        self.logger.info(f"chromosome = {decoded_string}, fitness score = {fitness_score}")

        self.fitness_score = fitness_score

    def __str__(self):
        r"""String representation"""
        return ("Chromosome_PhraseGeneration(Chromosome) \n "
                "\tgenotypes = {0}, \n"
                "\tfitness_score = {1}, \n"
                "\tnormalized_fitness_score = {2}".format(self._short_repr(), self.fitness_score, self.normalized_fitness_score))

    def _short_repr(self):
        r"""Short representation of the chromosome"""
        decoded_string = ""
        for geno in self._genotypes:
            decoded_string += geno.decoded_value

        return decoded_string