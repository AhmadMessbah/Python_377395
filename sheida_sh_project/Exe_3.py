#a program that gets 5 scores and gives the average of it

sum_num = 0

for i in range(5):
    score = float(input("Enter a score: "))
    sum_num += score
average = sum_num/5
print("average=",average)