import davipy as dv


# single number example
number = 13
print(dv.iseven(number))  # excepted result: False


# number list example
odds, evens = [], []
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    if dv.isodd(number):
        odds.append(number)
    else:
        evens.append(number)

print(evens)  # excepted result [2, 4, 6, 8, 10]
print(odds)  # excepted result [1, 3, 5, 7 , 9]
