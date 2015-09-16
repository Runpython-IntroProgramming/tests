from random import randint, seed

seed()
terms = randint(10,100)
sigfigs = randint(6,15)
print("{0}\n{1}\n".format(terms, sigfigs))
