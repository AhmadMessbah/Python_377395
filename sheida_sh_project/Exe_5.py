even_num = []
odd_num = []

while True:
    num=int(input("Enter a number: "))

    if num == 0:
        break

    if num % 2 == 0:
        even_num.append(num)
    else:
        odd_num.append(num)

print("even_num=",even_num)
print("odd_num=",odd_num)