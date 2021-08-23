from genetic.genotype import Genotype
from .phenotype import Phenotype_PhraseGeneration

class Genotype_PhraseGeneration(Genotype):
    r""" Genotype class for phrase generation example
    """
    def __init__(self, value):
        super().__init__(value)
        self.decoded_value = Phenotype_PhraseGeneration(self._value)._decode()

    def __str__(self):
        r"""String representation"""
        return ("Genotype_PhraseGeneration(Genotype) \n"
                "\tvalue = {0}, \n"
                "\tdecoded_value = ".format(self._value, self.decoded_value))