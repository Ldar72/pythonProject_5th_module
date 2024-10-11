class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        obj = super(House, cls).__new__(cls)
        cls.houses_history.append(args[0])
        return obj

    def __init__(self, name, floors):
        self.name = name
        self.floors = floors
        self.current_floor = 1

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

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")


house1 = House('ЖК Эльбрус', 30)
print(House.houses_history)
house2 = House('ЖК Изумруд', 6)
print(House.houses_history)
house3 = House('ЖК Эверест', 45)
print(House.houses_history)
del house2
del house3
print(House.houses_history)