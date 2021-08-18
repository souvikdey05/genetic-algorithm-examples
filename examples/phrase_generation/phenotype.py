from typing import List

from genetic.phenotype import Phenotype


class Phenotype_PhraseGeneration(Phenotype):
    r"""Phenotype class for phrase generation example"""

    def __init__(self, value):
        super().__init__(value)

    def _decode(self):
        # Here the gene value is the phenotype of the genotype
        return self._value