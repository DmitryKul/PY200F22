from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Неправильный тип данных")
        if capacity_volume<= 0:
            raise ValueError("Число не должно быть отрицательными")

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Неправильный тип данных")
        if occupied_volume<= 0:
            raise ValueError("Число не должно быть отрицательными")

        if occupied_volume > capacity_volume:
            raise ValueError("Заполняемый объём не должен быть больше вместимости") # Можно писать и TypeError

        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume


if __name__ == "__main__":
    glass_1 = Glass(200, 100) # TODO инициализировать два объекта типа Glass
    print(glass_1)
     # TODO попробовать инициализировать не корректные объекты
