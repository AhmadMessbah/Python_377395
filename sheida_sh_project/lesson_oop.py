class Lesson:
    def __init__(self, code, name, teacher):
        self.code = code
        self.name = name
        self.teacher = teacher

    def get_code(self):
        return self.__code

    def set_code(self, new_code):
        if not isinstance(new_code, int):
            raise TypeError("Invalid Code !")
        self.__code = new_code

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("Invalid Name !")
        self.__name = new_name

    def get_teacher(self):
        return self.__teacher

    def set_teacher(self, new_teacher):
        if not isinstance(new_teacher, str):
            raise TypeError("Invalid Teacher !")
        self.__teacher = new_teacher

    code = property(get_code, set_code)
    name = property(get_name, set_name)
    teacher = property(get_teacher, set_teacher)

    def save(self):
        print("Lesson saved:", self.code, self.name, self.teacher)

    def edit(self, new_name, new_teacher):
        self.name = new_name
        self.teacher = new_teacher


# ----------------------------------------------------------

lesson1 = Lesson(101, "Physics", "Abassi")
lesson1.save()

lesson1.edit("Optics", "Karimi")
print(lesson1.name, lesson1.teacher)