numbersList = [0,1,2,3,4];

for i in range(0,5):
    numbersList[i] = int(input("Number: "))

averageNumber = sum(numbersList) / len(numbersList)

print("The first number is {}".format(numbersList[0]))
print("The last number is {}".format(numbersList[4]))
print("The smallest number is {}".format(min(numbersList)))
print("The biggest number is {}".format(max(numbersList)))
print("The average number is {}".format(averageNumber))


print(numbersList)