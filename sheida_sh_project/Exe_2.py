#a program that calculate the average digits that divided to 2,7

number = int(input("Enter a number: "))

sum_num = 0
count = 0

for i in range(1,number+1):
    if i % 2 ==0 and i % 7 ==0:
        sum_num += i
        count += 1

if count > 0:
    print(sum_num)
    print(count)
    print("average", sum_num/count)
else:
    print("invalid")

