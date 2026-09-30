from parking_module import show_menu, get_car_infos, print_parking_list, find_car_by_plate

parking_list = []

while True:
    option = show_menu()
    print("--------------------------------")

    match option:
        case 1:
            car = get_car_infos()
            if find_car_by_plate(parking_list, car["plate"]):
                print("error: car already exists")
            else:
                parking_list.append(car)
                print("info: car added to parking list")
        case 2:
            print_parking_list(parking_list)
        case 3:
            plate = input("enter the plate number for search: ")
            result = find_car_by_plate(parking_list, plate)
            if result:
                print("found:", result)
            else:
                print("error: car not found")
        case 0:
            break
        case _:
            print("error: Invalid option")

    print("--------------------------------")