expenses = [10.50, 8, 5 ,15, 20, 5, 3]

total = sum(expenses)

print("You spent $", total, sep = "")

expenses2 = []
total2 = 0

for i in range(7):
    expenses2.append(float(input("Enter an expanse:\n")))

total2 = sum(expenses2)

print("You spent $", total2, sep="")


expenses3 = []
total3 = 0
num_expenses = int(input("Enter # of expenses:\n"))

for i in range(num_expenses):
    expenses3.append(float(input("Enter an expense:")))

total3 = sum(expenses3)

print("You spent $", total3, sep="")