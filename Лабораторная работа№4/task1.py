class Cars:
    """Базовый класс автомобилей"""

    def __init__(self, brand: str, num_of_seats: int, colour: str, horsepower: int):
        self._brand = brand # марку автомобиля изменить нельзя
        self._num_of_seats = num_of_seats # количество посадочных мест изменить нельзя
        self.colour = colour # цвет можно изменять
        self.horsepower = horsepower

    def __str__(self):
        return f"Автомобиль марки {self.brand}. Количество посадочных мест {self.num_of_seats}. Цвет {self.colour}. Лошадиные силы {self.horsepower}"

    def __repr__(self):
        return f"{self.__class__.__name__}(brand={self.brand!r}, num_of_seats={self.num_of_seats!r}, colour:{self.colour!r}. horsepower:{self.horsepower!r})"

    def change_colour(self, colour):
        """Метод, который изменяет цвет автомобиля

        :return новый цвет автомобиля

        Пример: Cars("BMW", 5, "Red", 170)

        Cars.change_colour(Blue)

        """

    def horsepower_upgrade(self, horsepower):
        """Метод, каоторый увеличичает количество лошадиных сил

        :return увеличенное количество лошадиных сил

        Пример: Cars("BMW", 5, "Red", 170)

        Cars.horsepower_upgrade(210)

        """

    @property
    def brand(self):
        return self._brand

    @property
    def num_of_seats(self):
        return self._num_of_seats


class PassengerCar(Cars):
    """Дочерний класс легковых автомобилей"""

    def __init__(self, brand: str, num_of_seats: int, colour: str, horsepower: int, trunk_vol: float): # trunk_vol- объем багажника
        super().__init__(brand, num_of_seats, colour, horsepower)
        self._trunk_vol = trunk_vol # объем багажника изменить нельзя

    @property
    def trunk_vol(self):
        return self._trunk_vol

    def __str__(self):
        return f"Автомобиль марки {self.brand}. Количество посадочных мест {self.num_of_seats}. Цвет {self.colour}. Лошадиные силы {self.horsepower}. Объем багажника {self.trunk_vol}"

    def __repr__(self):
        return f"{self.__class__.__name__}(brand={self.brand!r}, num_of_seats={self.num_of_seats!r}, colour:{self.colour!r}, horsepower:{self.horsepower!r}, trunk_vol{self.trunk_vol})"

    # методы change_colour и horsepower_upgrade унаследованы
    # методы __str__ и __repr__ перегружены, так как добавлен атрибут _trunk_vol



class Truck(Cars):
    """Дочерний класс грузовых автомобилей"""


    def __init__(self, brand: str, num_of_seats: int, colour: str, horsepower: int):
        super().__init__(brand, num_of_seats, colour, horsepower)

    def horsepower_upgrade(self, horsepower):
        """Метод, каоторый увеличичает количество лошадиных
        пергруден для грузовых автомобилей и не будет давать возможность
        этому классу увеличивать количество лошидиных сил, так как чеще всего
        такакя возможность ограничена законом. То есть метод не даст изменить количество
        лошадиных сил у грузового автомобиля"""

    # методы change_colour, __str__ и __repr__ унаследованы


if __name__ == "__main__":

    car_1 = PassengerCar("BMW", 5, "RED", 210, 520.3)
    print(car_1)
    car_2 = Truck("Камаз", 3, "Black", 180)
    print(car_2)
    pass
