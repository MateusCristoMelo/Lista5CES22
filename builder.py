from abc import ABC, abstractmethod

class CakeBuilder(ABC):
    """Classe abstrata builder do bolo"""

    @property
    @abstractmethod
    def product(self):
        pass

    @abstractmethod
    def cake_occasion(self):
        pass

    @abstractmethod
    def make_cake_dough(self):
        pass

    @abstractmethod
    def make_cake_cover(self):
        pass

class ChocolateCake(CakeBuilder):
    """Classe bolo de chocolate"""

    def __init__(self):
        self.reset()

    def reset(self):
        self._product = Cake()

    @property
    def product(self):
        product = self._product
        self.reset()
        return product

    def cake_occasion(self):
        self._product.add("Birthday")

    def make_cake_dough(self):
        self._product.add("ChocolateDough")

    def make_cake_cover(self):
        self._product.add("ChocolateCover")

class CarrotCake(CakeBuilder):
    """Classe bolo de cenoura"""

    def __init__(self):
        self.reset()

    def reset(self):
        self._product = Cake()

    @property
    def product(self):
        product = self._product
        self.reset()
        return product

    def cake_occasion(self):
        self._product.add("Wedding")

    def make_cake_dough(self):
        self._product.add("CarrotDough")

    def make_cake_cover(self):
        self._product.add("CarrotCover")


class Cake():
    """Classe bolo"""
    
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

class Director:
    """Classe diretor"""

    def __init__(self):
        self._builder = None

    @property
    def builder(self):
        return self._builder

    @builder.setter
    def builder(self, CakeBuilder):
        self._builder = CakeBuilder

    def build_cake(self):
        self.builder.make_cake_dough()
        self.builder.make_cake_cover()
        self.builder.cake_occasion()

if __name__ == "__main__":

    director = Director()
    director.builder = ChocolateCake()