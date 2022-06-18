from abc import ABC, abstractmethod

class CakeFactory(ABC):
    """Classe abstrata fabrica de bolo"""

    @abstractmethod
    def make_cake_dough(self):
        pass

    @abstractmethod
    def make_cake_cover(self):
        pass

class ChocolateFactory(CakeFactory):
    """Classe fabrica de bolo de chocolate"""

    def make_cake_dough(self):
        return ChocolateDough()

    def make_cake_cover(self):
        return ChocolateCover()

class CarrotFactory(CakeFactory):
    """Classe fabrica de bolo de cenoura"""

    def make_cake_dough(self):
        return CarrotDough()

    def make_cake_cover(self):
        return CarrotCover()

class OccasionFactory(CakeFactory):
    """Classe fabrica ocasiao"""

    def cake_occasion(self):
         return OccasionCake()

class OccasionCake(ABC):
    """Classe abstrata ocasiao"""

    @abstractmethod
    def show(self):
        pass

class BirthdayOccasion(OccasionCake):
    """Classe ocasiao aniversario"""

    def show(self):
        print("Birthday Occasion.")

class WeddingOccasion(OccasionCake):
    """Classe ocasiao casamento"""
        
    def show(self):
        print("Wedding Occasion.")

class ChocolateCake(ABC):
    """Classe bolo de chocolate"""

    @abstractmethod
    def show(self):
        pass

class ChocolateDough(ChocolateCake):
    """Classe massa de chocolate"""

    def show(self):
        print("Chocolate Dough.")

class ChocolateCover(ChocolateCake):
    """Classe cobertura de chocolate"""

    def show(self):
        print("Chocolate Cover.")

class CarrotCake(ABC):
    """Classe bolo de cenoura"""

    @abstractmethod
    def show(self):
        pass

class CarrotDough(ChocolateCake):
    """Classe massa de cenoura"""

    def show(self):
        print("Carrot Dough.")

class CarrotCover(ChocolateCake):
    """Classe cobertura de cenoura"""
    
    def show(self):
        print("Carrot Cover.")

def user_order(CakeFactory):
    """Classe ordens do usuario"""

    CakeFactory.make_cake_cover().show()
    CakeFactory.make_cake_dough().show()

if __name__ == "__main__":

    user_order(ChocolateFactory())
    user_order(CarrotFactory())