# program to find largest number in a list
numbers = [1,4,9,22,6,7,10]
max = numbers[0]
for number in numbers:
    if number> max:
        max = number
print(max)