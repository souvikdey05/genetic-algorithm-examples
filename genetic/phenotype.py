from abc import ABC, abstractmethod

class Phenotype(ABC):
    r""" The Base Phenotype class
    """
    def __init__(self, value):
        self._value = value   # Decode this gene infomration

    @abstractmethod
    def _decode(self):
        pass