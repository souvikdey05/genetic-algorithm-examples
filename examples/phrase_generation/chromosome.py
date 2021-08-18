from genetic.chromosome import Chromosome

class Chromosome_PhraseGeneration(Chromosome):
    r"""Chromosome class for phrase generation example"""

    def __init__(self, genotypes, fitness_score=0.0):
        super().__init__(genotypes, fitness_score)

    def _crossover(self, partner):
        r"""Performs crossover between two chromosomes"""
        print("crossover")

        return None

    def _mutate(self, mutation_rate):
        r"""Performs mutation based on mutation rate"""
        print("mutation")
        return None

    def _calculate_fitness_score(self, fitness_fn):
        f"""Calculates the fitness score of this Chromosome based on the fitness function"""
        print("calculating fitness score")

        decoded_string = ""
        for geno in self._genotypes:
            decoded_string += geno.decoded_value

        return fitness_fn(decoded_string)