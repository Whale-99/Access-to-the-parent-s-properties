# Базовый класс для всех транспортных средств
class Vehicle:
    # Допустимые цвета для окрашивания транспорта
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner               # Владелец транспортного средства
        self.__model = model             # Модель транспортного средства
        self.__color = color             # Цвет транспортного средства
        self.__engine_power = engine_power  # Мощность двигателя

    # Метод возвращает название модели
    def get_model(self):
        return f"Модель: {self.__model}"

    # Метод возвращает мощность двигателя
    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    # Метод возвращает цвет транспортного средства
    def get_color(self):
        return f"Цвет: {self.__color}"

    # Метод выводит полную информацию о транспортном средстве
    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    # Метод позволяет сменить цвет, если он в списке разрешенных цветов
    def set_color(self, new_color):
        if new_color.lower() in [color.lower() for color in self.__COLOR_VARIANTS]:
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")

# Класс Sedan, унаследованный от Vehicle
class Sedan(Vehicle):
    # Максимально допустимое количество пассажиров
    __PASSENGERS_LIMIT = 5

# Проверка работы программы
# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Vlad', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')    # Нельзя сменить цвет на Pink
vehicle1.set_color('BLACK')   # Установка цвета 'BLACK'
vehicle1.owner = 'Ivan'     # Смена владельца

# Проверяем что поменялось
vehicle1.print_info()
