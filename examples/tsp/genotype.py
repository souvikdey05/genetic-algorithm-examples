from genetic.genotype import Genotype
from .phenotype import Phenotype_TSP

class Genotype_TSP(Genotype):
    r""" Genotype class for TSP example
    """
    def __init__(self, value):
        super().__init__(value)
        self.decoded_value = Phenotype_TSP(self._value)._decode()

    def __str__(self):
        r"""String representation"""
        return ("Genotype_TSP(Genotype) \n"
                "\tvalue = {0}, \n"
                "\tdecoded_value = ".format(self._value, self.decoded_value))