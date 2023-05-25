import davipy as dv #import the library

#define your number or list of numbers
number = 13
list_of_numbers = [1,2,3,4,5,6,7,8,9,10]


#you can check if its even
print(dv.iseven(number))
#It will print you "False"



#you can even use the function is a for

#define your list of odds
list_odds = []
#define your list of evens
list_evens = []

for number in list_of_numbers:
    if dv.isodd(number):
        list_odds.append(number)
    else:
        list_evens.append(number)

print(list_evens)
print(list_odds)
        


