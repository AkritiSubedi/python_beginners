numbers = [5, 2, 1, 5, 3, 5, 7, 4]
numbers.insert(0, 10)
numbers.remove(2)
numbers.sort()
numbers.reverse()
print(numbers)
print(numbers.sort())


# program to remove duplicates in a list

number = [5, 2, 1, 2, 2, 4, 6, 4, 5, 1]
uniques = []
for numbers in number:
    if numbers not in uniques:
        uniques.append(numbers)
print(uniques)