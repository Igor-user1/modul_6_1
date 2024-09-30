class Animal:
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        if food.edible is True:
            self.fed = True
            return f'{self.name} съел {food.name}'
        else:
            self.alive = False
            return f'{self.name} не стал есть {food.name}'


class Plant:
    edible = False

    def __init__(self, name):
        self.name = name


class Mammal(Animal):

    def __init__(self, name):
        super().__init__(name)


class Predator(Animal):

    def __init__(self, name):
        super().__init__(name)


class Flower(Plant):
    edible = False

    def __init__(self, name):
        super().__init__(name)


class Fruit(Plant):
    edible = True

    def __init__(self, name):
        super().__init__(name)


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
print(a1.eat(p1))
print(a2.eat(p2))
print(a1.alive)
print(a2.fed)
