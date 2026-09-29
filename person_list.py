student_list = []
for i in range(3):
    name = input("Please enter your name: ")
    family = input("Please enter your family name: ")
    age = input("Please enter your age: ")
    years = input("Please enter your years: ")
    month = input("Please enter your months: ")
    days = input("Please enter your days: ")
    birth_date = input("year,month,day: ")

    student={"name":name,"family": family,"age": age,"years":years,"month": month,"day": days,"birth_date": birth_date}
    student_list.append(student)
    print("student_list",student)

print("student_list:")
