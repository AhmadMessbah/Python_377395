
number = int(input("Enter a number: "))
if number>=0:
    for i in range(-number,number+1,1):
        print(i)

else:
    for i in range(number,number-1,-1):
        print(i)