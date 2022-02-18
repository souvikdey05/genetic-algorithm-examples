from genetic.phenotype import Phenotype

class Phenotype_TSP(Phenotype):
    r"""Phenotype class for tsp example"""

    def __init__(self, value):
        super().__init__(value)

    def _decode(self):
        r"""How to decode the genotype value?"""
        # Here the gene value is the phenotype of the genotype
        return f"City={self._value}"