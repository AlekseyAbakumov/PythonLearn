class Planet:
    """Классы Планета"""

    def __init__(self, name):
        self.name = name

    # этот метод не обязательный. Он говорит о том, что если идет обращение
    # к экземпляру класса, без указания атрибу, то, чтобы возвращал указанны
    # атрибут. В данном случае имя класса


solar_system=[]

planet_names=[
    "Меркурий", "Венера", "Земля", "Марс", "Юпитер", "Сатурн", "Уран", "Нептун"
]

# Создаем сразу все планеты солнечной системы
for name in planet_names:
    print(name)
    name=Planet(name)
    print(name)
    solar_system.append(name)

