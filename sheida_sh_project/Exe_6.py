odd_num = 0
sum_num = 0

while True:
    number = int(input("Enter a number: "))

    if number == 0:
        break

    if number % 2 != 0:
       odd_num.append(number)


for i in odd_num:
    sum_num += i

if len(odd_num) > 0:
    print("Average=",sum_num/len(odd_num))
else:
    print("No odd number")