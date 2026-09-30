MAX_UNIT = 17

lessons = []
sum_unit = 0

while sum_unit <= MAX_UNIT:
    title = input("title: ")
    teacher = input("teacher: ")
    duration = input("duration: ")
    unit = int(input("unit: "))

    lesson = {
        "title": title,
        "teacher": teacher,
        "duration": duration,
        "unit": unit,
    }

    lessons.append(lesson)
    sum_unit += unit

print("\nlessons:")

for lesson in lessons:
    print(f"title: {lesson['title']}")
    print(f"teacher: {lesson['teacher']}")
    print(f"duration: {lesson['duration']}")
    print(f"unit: {lesson['unit']}")
    print("-------------")