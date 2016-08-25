def main():
    incomes = []
    NumberOfMonths = int(input("How many months? "))

    for month in range(1, NumberOfMonths + 1):
        income = float(input("Enter income for month {}: ".format(str(month))))
        incomes.append(income)
    printReport(NumberOfMonths,incomes,income)

def printReport(NumberOfMonths,incomes,income):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, NumberOfMonths + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()