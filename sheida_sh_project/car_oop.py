class Car:
    def __init__(self, name, color, plate):
        self.name = name
        self.color = color
        self.plate = plate

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("Invalid Name !")
        self.__name = new_name

    def get_color(self):
        return self.__color

    def set_color(self, new_color):
        if not isinstance(new_color, str):
            raise TypeError("Invalid Color !")
        self.__color = new_color

    def get_plate(self):
        return self.__plate

    def set_plate(self, new_plate):
        if not isinstance(new_plate, str):
            raise TypeError("Invalid Plate !")
        self.__plate = new_plate

    name = property(get_name, set_name)
    color = property(get_color, set_color)
    plate = property(get_plate, set_plate)

    def save(self):
        print("Car saved:", self.name, self.color, self.plate)

    def change_plate(self, new_plate):
        self.plate = new_plate


# ----------------------------------------------------------

car1 = Car("Pride", "white", "12A345")
car1.save()

car1.change_plate("45B678")
print(car1.plate)