class Device:
    def __init__(self, name):
        self.name = name

    def info(self):
        print("Device:", self.name)

class Electric(Device):
    def __init__(self, name):
        super().__init__(name)

    def power(self):
        print(self.name, "uses electricity")

class NonElectric(Device):
    def __init__(self, name):
        super().__init__(name)

    def use(self):
        print(self.name, "does not use electricity")


class Computer(Electric):
    def __init__(self, name, ram, cpu):
        super().__init__(name)
        self.ram = ram
        self.cpu = cpu

    def info(self):
        print(self.name, self.ram, self.cpu)


class Mobile(Electric):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size


class Iphon(Mobile):
    def __init__(self, name, size, model):
        super().__init__(name, size)
        self.model = model

    def info(self):
        print(self.model, "Iphon")


class Summsong(Mobile):
    def __init__(self, name, size, model):
        super().__init__(name, size)
        self.model = model

    def info(self):
        print(self.model, "Summsong")


class Furniture(NonElectric):
    def __init__(self, name, size, color):
        super().__init__(name)
        self.size = size
        self.color = color

    def info(self):
        print(self.name, self.size, self.color) 