from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, size):
        self.size = size

    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    @property
    def consumption(self):
        V = self.size
        # return f"Расход ткани на пальто (рост {V}) составит: {round(V / 6.5 + 0.5, 2)}"
        return round(V / 6.5 + 0.5, 2)


class Suit(Clothes):
    @property
    def consumption(self):
        H = self.size
        # return f"Расход ткани на костюм (размер {H}) составит: {2 * H + 0.3}"
        return 2 * H + 0.3


coat1 = Coat(1.8)
suit1 = Suit(0.52)

# print(coat1.consumption)
# print(suit1.consumption)
print(f"Суммарный расход ткани составит: {coat1.consumption + suit1.consumption}")
