import davipy as dv


# single number example
number = 13
print(dv.isprime(number))  # excepted result: True


# number list example
numbers = [31, 12, 233, 124, 115, 46, 17, 33, 46, 79, 17]
primes = []

for number in numbers:
    if dv.isodd(number):  # TODO concettualmente sbagliato, se ne hai bisogno dovresti spostare il controllo in .isprime()
        if dv.isprime(number):
            primes.append(number)

print(primes)
