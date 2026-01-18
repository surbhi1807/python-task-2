# Program to print all positive numbers in a list

list1 = [12, -7, 5, 64, -14]
list2 = [12, 14, -95, 3]

print("Positive numbers from list1:")
for num in list1:
    if num > 0:
        print(num, end=" ")

print("\n")

print("Positive numbers from list2:")
positive_list2 = []
for num in list2:
    if num > 0:
        positive_list2.append(num)

print(positive_list2)
