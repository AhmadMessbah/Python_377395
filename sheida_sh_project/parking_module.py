parking_list = []


def show_menu():
    print("1) Enter to parking")
    print("2) parking list")
    print("3) search car by plate")
    print("0) Exit")
    option = int(input("option: "))
    return option


def get_car_infos():
    name = input("Enter car name: ")
    color = input("Enter car color: ")
    plate = input("Enter car plate: ")
    enter_time = input("Enter car enter time: ")

    return {"name": name, "color": color, "plate": plate, "enter_time": enter_time}


def print_parking_list(parking_list):
    for car in parking_list:
        print(f"{car['name']:10} {car['plate']:10} {car['enter_time']:10} {car['color']:10}")


def find_car_by_plate(parking_list, plate):
    for car in parking_list:
        if car["plate"] == plate:
            return car

    return None