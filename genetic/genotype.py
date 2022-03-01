from abc import ABC, abstractmethod

from .phenotype import Phenotype

class Genotype(ABC):
    r""" The Base Genotype class
    """
    def __init__(self, value):
        self._value = value

    def get_value(self):
        return self._value