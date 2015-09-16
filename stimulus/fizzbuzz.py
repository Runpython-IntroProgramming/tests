import fractions
from random import randint

terms = randint(60,80)
fizzbuzz = lambda x=15 : randint(3,x)
fizzn = fizzbuzz()
buzzn = fizzbuzz(terms//fizzn)
while (fizzn == buzzn or
    not fizzn % buzzn  or
    not buzzn % fizzn or
    fractions.gcd(buzzn, fizzn) == 1):
    fizzn = fizzbuzz()
    buzzn = fizzbuzz(terms//fizzn)
print("{0}\n{1}\n{2}\n".format(terms, fizzn, buzzn))
