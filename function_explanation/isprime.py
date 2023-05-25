import davipy as dv #import the library

#define your number or list of numbers
number = 13
list_of_numbers = [31,12,233,124,115,46,17,33,46,79,17]


#you can check if its prime
print(dv.isprime(number))
#It will print you "True"



#you can even use the function is a for

#define you list of primes
list_primes = []

for number in list_of_numbers:
    if dv.isodd(number):
        if dv.isprime(number):
            list_primes.append(number)

print(list_primes)