class Product:  # کالا
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show(self):
        print("Name:", self.name, "| Price:", self.price)


# ---------- شاخه برقی ----------
class Electrical(Product):  # برقی
    def __init__(self, name, price, voltage):
        self.name = name
        self.price = price
        self.voltage = voltage

    def show(self):
        print("Name:", self.name, "| Price:", self.price)
        print("Voltage:", self.voltage)


class Mobile(Electrical):  # موبایل
    def __init__(self, name, price, voltage, screen_size):
        self.name = name
        self.price = price
        self.voltage = voltage
        self.screen_size = screen_size

    def show(self):
        print("Name:", self.name, "| Price:", self.price)
        print("Voltage:", self.voltage)
        print("Screen size:", self.screen_size, "inch")


class Apple(Mobile):  # اپل
    def __init__(self, name, price, voltage, screen_size, series):
        self.name = name
        self.price = price
        self.voltage = voltage
        self.screen_size = screen_size
        self.series = series

    def show(self):
        print("Name:", self.name, "| Price:", self.price)
        print("Voltage:", self.voltage)
        print("Screen size:", self.screen_size, "inch")
        print("Series:", self.series)


class Samsung(Mobile):  # سامسونگ
    def __init__(self, name, price, voltage, screen_size, series):
        self.name = name
        self.price = price
        self.voltage = voltage
        self.screen_size = screen_size
        self.series = series

    def show(self):
        print("Name:", self.name, "| Price:", self.price)
        print("Voltage:", self.voltage)
        print("Screen size:", self.screen_size, "inch")
        print("Series:", self.series)


class Laptop(Electrical):  # لپ‌تاپ
    def __init__(self, name, price, voltage, ram, cpu):
        self.name = name
        self.price = price
        self.voltage = voltage
        self.ram = ram
        self.cpu = cpu

    def show(self):
        print("Name:", self.name, "| Price:", self.price)
        print("Voltage:", self.voltage)
        print("RAM:", self.ram, "| CPU:", self.cpu)


# ---------- شاخه غیربرقی ----------
class NonElectrical(Product):  # غیربرقی
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def show(self):
        print("Name:", self.name, "| Price:", self.price)
        print("Weight:", self.weight)


class Furniture(NonElectrical):  # مبلمان
    def __init__(self, name, price, weight, seats, color):
        self.name = name
        self.price = price
        self.weight = weight
        self.seats = seats
        self.color = color

    def show(self):
        print("Name:", self.name, "| Price:", self.price)
        print("Weight:", self.weight)
        print("Seats:", self.seats, "| Color:", self.color)


# ------- تست -----
# سامسونگ A21، صفحه 8 اینچ، 220 ولت
phone = Samsung("Galaxy", 10000000, 220, 8, "A21")
phone.show()

print("------------------------------")

# مبل 7 نفره صورتی
sofa = Furniture("Sofa", 25000000, 60, 7, "pink")
sofa.show()