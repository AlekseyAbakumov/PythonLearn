class Planet:
    """This class desctibes plantes"""

    count = 1

    def __init__(self, name, population=None):
        self.name = name
        # Население
        self.population = population or []


planet = Planet("Earth")

print(planet.__dict__)

# На лету добавляем новый метод экземпляру. МАССА
planet.mass = 5_000_000

print(planet.__dict__)
print("")
print(Planet.__dict__)
print("")
print(Planet.__doc__)
print("")
print(planet.__doc__)
print("")
print(dir(planet))
print("")
print(planet.__class__)