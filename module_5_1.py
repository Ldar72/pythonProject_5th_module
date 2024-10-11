class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if not isinstance(new_floor, int) or new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
        else:
            for floor in range(1, new_floor + 1):
                print(floor)


house1 = House('ЖК Приморский', 9)
house2 = House('ЖК Изумруд', 6)

# print(house1.name)
# print(house1.number_of_floors)
# print(house2.name)
# print(house2.number_of_floors)

house1.go_to(1)
house1.go_to(15)
house2.go_to(2)
house2.go_to(-1)
