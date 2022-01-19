# ООП
# Объекты

# class Player:
#     def __init__(self, health, power):
#         # Приватное поле (недоступно вне текущего класса)
#         self.__health = health
#         self.__power = power
#         self.__stamina = 100

#     def action(self):
#         print('ACT')
    
#     def attack(self, player):
#         # ! self.action() - методы видят друг друга только через self
#         player.__health -= self.__power
#         self.__health -= (player.__power / 2)

#     def  __str__(self) -> str:
#         return 'health: %.2f, power: %.2f, stamina: %.2f' % (self.__health, self.__power, self.__stamina)

#     # pass

# player1 = Player(health=100, power=200)
# # player1.__health = ... - запрещен, т.к. приватное поле
# player2 = Player(150, 100)

# print('Before fighting')
# print(player1)
# print(player2)

# player1.attack(player2)

# print('After fighting')
# print(player1)
# print(player2)

# Пример наследования


class Car:
    def __init__(self, color, model):
        self._color = color
        self._model = model
        self._energy = 100
    
    def run(self, speed):
        self._energy -= speed
    
    def get_energy(self) -> float:
        return self._energy
    
    def turn_off(self):
        print('*** Car turned off ***')
        
    def get_model(self) -> str:
        return self._model
    
    def get_color(self) -> str:
        return self._color
        
    
# Inheritance - наследование, inherits - наследовать
# class ModernCar(Car):
#     pass

class ModernCar(Car):
    # public protected private
    def __init__(self, color, model, roof=True):
        # super - обращение к базовому классу
        super().__init__(color, model)
        self._roof = roof
        # self._energy = 1000
        # self.public_field = 10
        # self._protected_field = 11
        # self.__private_field = 12
        
    # redifinition - переопределение в дочернем классе
    def run(self, speed):
        self._energy -= 0.1 * speed

    # extend - расширяем поведение базового класса
    def turn_off(self):
        super().turn_off()
        print('*** Windows closed ***')

    def has_roof(self) -> bool:
        return self._roof        
    
    # def foo(self):
        # self.__private_field = 10  -  OK


# class Foo:
#     # Конструктор есть всегда
#     def __init__(self):
#         pass

# old = Car('red', 'Opel')
# print(old.get_model())
# old.run(10)
# print(old.get_energy())
# old.turn_off()

# m = ModernCar('blue', 'Reno')
# print(m.get_model())
# m.turn_off()
# m.run(10)
# print(m.get_energy())
# print(m.public_field)
# m.public_field = 200

# 3 кита ООП
# - Наследование (inheritance)
# - Инкапсуляция (encapsulation) - свойство класса хранить в себе и атрибуты, и методы воедино
# - Полиморфизм (polymorphism) - свойство класса переопределять поведение базового класса

# abstract class - класс, экземпляры которого нельзя создать
# class Musician:
#     def play(self):
#         pass


# class Pianist(Musician):
#     def play(self):
#         print('Push the button')


# class Violinist(Musician):
#     def play(self):
#         print('Creak')


# class Vocalist(Musician):
#     def play(self):
#         print('Sing: Ave Maria')


# from typing import List

# Пример полиморфизма

# orchestra: List[Musician] = [Pianist(), Violinist(), Vocalist(), Pianist()]
# choose = int(input('0-1-2: '))
# if choose == 0:
#     orchestra.append(Pianist())
# elif choose == 1:
#     orchestra.append(Violinist())
# else:
#     orchestra.append(Vocalist())
# # exception if choose not in [0, 1, 2]

# for musician in orchestra:
#     musician.play()
    
# Наследник должен обладать всеми атрибутами базового класса


# class Mom:
#     def foo(self):
#         print(1)
        
# class Dad:
#     def foo(self):
#         print(2)
        
# # "Главнее" тот метод, класс которого находится левее в скобках наследования
# class Son(Mom, Dad):
#     pass

# class SomethingMixin

# s = Son()
# s.foo()