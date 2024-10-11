class House:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def go_to(self, new_floor):
        if not isinstance(new_floor, int) or new_floor > self.floors or new_floor < 0:
            print("Такого этажа не существует")
        elif new_floor == self.current_floor:
            pass
        else:
            self.current_floor = new_floor
            for floor in range(1, new_floor + 1):
                print(floor)

    def __len__(self):
        return self.floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.floors}"

    def __eq__(self, other):
        if not isinstance(other, House):
            raise TypeError("Сравнивать можно только здания.")
        return self.floors == other.floors

    def __lt__(self, other):
        if not isinstance(other, House):
            raise TypeError("Сравнивать можно только здания.")
        return self.floors < other.floors

    def __le__(self, other):
        if not isinstance(other, House):
            raise TypeError("Сравнивать можно только здания.")
        return self.floors <= other.floors

    def __gt__(self, other):
        if not isinstance(other, House):
            raise TypeError("Сравнивать можно только здания.")
        return self.floors > other.floors

    def __ge__(self, other):
        if not isinstance(other, House):
            raise TypeError("Сравнивать можно только здания.")
        return self.floors >= other.floors

    def __ne__(self, other):
        if not isinstance(other, House):
            raise TypeError("Сравнивать можно только здания.")
        return self.floors != other.floors

    def __add__(self, value):
        if not isinstance(value, int):
            raise TypeError("Введите целое число.")
        new_floors = self.floors + value
        return House(self.name, new_floors)

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)


house1 = House('ЖК Приморский', 9)
house2 = House('ЖК Изумруд', 6)

print(house1)
print(house2)
print(house1 == house2)  # __eq__
house1 = house1 + 10  # __add__
print(house1)
print(house1 == house2)
house1 += 10  # __iadd__
print(house1)
house2 = 10 + house2  # __radd__
print(house2)
print(house1 > house2)  # __gt__
print(house1 >= house2)  # __ge__
print(house1 < house2)  # __lt__
print(house1 <= house2)  # __le__
print(house1 != house2)  # __ne__
