from genetic.genotype import Genotype

class Genotype_PhraseGeneration(Genotype):
    r""" Genotype class for phrase generation example
    """
    def __init__(self, value):
        super().__init__(value)
        self.decoded_value = Phenotype_PhraseGeneration(self._value)._decode()