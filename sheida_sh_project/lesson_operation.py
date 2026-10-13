lesson_list = [
    {"name": "Python", "unit": 3, "teacher": "Ali"},
    {"name": "Python", "unit": 3, "teacher": "Reza"},
    {"name": "Java", "unit": 5, "teacher": "Ahmad"},
    {"name": "C#", "unit": 2, "teacher": "Omid"},
]

new_lesson = {"name": "Database", "unit": 3, "teacher": "Sara"}

unit_price = {
    2: 1000,
    3: 1200,
    5: 1400,
}

lesson_list.append(new_lesson)
print(lesson_list)


def sort_by_unit(lesson):
    return lesson["unit"]


def sort_by_teacher(lesson):
    return lesson["teacher"].lower()


lesson_list = sorted(lesson_list, key=sort_by_unit)
lesson_list = sorted(lesson_list, key=sort_by_teacher)
print(lesson_list)


def add_amount(lesson):
    lesson["amount"] = lesson["unit"] * unit_price[lesson["unit"]]
    return lesson


result = list(map(add_amount, lesson_list))
print(result)


def check_amount(lesson):
    return lesson["amount"] > 1200


filtered_result = list(filter(check_amount, result))
print(filtered_result)


def get_amount(lesson):
    return lesson["amount"]


amount_list = list(map(get_amount, result))
print(amount_list)
print("Sum Total :", sum(amount_list))