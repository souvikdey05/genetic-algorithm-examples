from .population import Population_PhraseGeneration
from .chromosome import Chromosome_PhraseGeneration
from .genotype import Genotype_PhraseGeneration

class Phrase_Generation:
    r"""Main class for Phrase generation example"""

    def __init__(self):
        genotype = Genotype_PhraseGeneration()
        genotypes = [genotype]

        chromosome = Chromosome_PhraseGeneration(genotypes)
        chromosomes = [chromosome]

        mutation = 0
        population = Population_PhraseGeneration(chromosomes, mutation)

    @staticmethod
    def main():
        print("In main")
        obj = Phrase_Generation()