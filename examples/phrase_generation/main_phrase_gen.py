import json
import string
import random

from .population import Population_PhraseGeneration
from .chromosome import Chromosome_PhraseGeneration
from .genotype import Genotype_PhraseGeneration

class Phrase_Generation:
    r"""Main class for Phrase generation example"""

    def __init__(self, population_size=20, mutation_rate=0.0, target_phrase=None, max_generations=None):
        
        self._population_size = population_size
        self._mutation_rate = mutation_rate
        self._target_phrase = target_phrase
        self._max_generations = max_generations
        
        string.ascii_letters = "abcdefghijklmnopqrstuvwxyz"  # Only lower case letters for now
        
        # generate multiple chromosomes for a population
        chromosomes = []
        for p in range(population_size):

            # generate genotype for each chromosome
            # the length of the target phrase gives the number of genotype for a chromosome
            genotypes = []
            for i in range(len(target_phrase)):
                geno = Genotype_PhraseGeneration(random.choice(string.ascii_letters))
                genotypes.append(geno)
            
            chromo = Chromosome_PhraseGeneration(genotypes)
            chromosomes.append(chromo)

        population = Population_PhraseGeneration(chromosomes, self._mutation_rate, target_phrase)
        self._population = population
        

    def run(self):
        pass
    
    @staticmethod
    def main(config_file):
        config = json.load(open(config_file))

        # Some validity checks
        if "target_phrase" not in config or config["target_phrase"] is None:
            raise Exception("You need to specify the target phrase to solve in config file")

        population_size = 20
        if "population_size" in config and config["population_size"] is not None:
            population_size = config["population_size"]

        mutation_rate = 0.0
        if "mutation_rate" in config and config["mutation_rate"] is not None:
            mutation_rate = config["mutation_rate"]

        max_generations = None
        if "max_generations" in config and config["max_generations"] is not None:
            max_generations = config["max_generations"]

        obj = Phrase_Generation(population_size, mutation_rate, target_phrase, max_generations)
        obj.run()