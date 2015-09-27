import random
random.seed()

assocs = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'"+chr(34)+"/"+chr(92)+"<>(){}[]-=_+?!") * 2
encode = lambda s: [assocs.find(c) for c in s]   # convert string to digits
decode = lambda l: ''.join([assocs[n] for n in l]) # digits to chars to string
keygen = lambda s, p: p*(len(s)//len(p)) + p[:len(s)%len(p)]    # generate a key of length = message
encrypt = lambda s, k: [(sc+kc)%len(assocs) for sc,kc in zip(s,k)] # encrypt text, using key
decrypt = lambda e, k: [(ec-kc)%len(assocs) for ec,kc in zip(e,k)]  # decrypt text, using key
samplestrings = ["How now? A rat? Dead, for a ducat, dead!",
  "Done to death by slanderous tongue",
  "Why then tonight let us assay our plot",
  "Thou art a votary to fond desire",
  "Some Cupid kills with arrows, some with traps",
  "Be not afraid of greatness",
  "Lord, what fools these mortals be",
  "Our remedies oft in ourselves do lie",
  "I go, and it is done; the bell invites me"]
samplekeys = ["password", 
  "123456", 
  "12345678", 
  "abc123",
  "qwerty",
  "monkey",
  "letmein",
  "dragon",
  "111111",
  "baseball"]

unrecognizedi = random.randint(0,5)
for i in range(0,6):
    if i == unrecognizedi:
        print(random.choice('lmnoprs'))
    else:
        t = random.choice(samplestrings)
        p = random.choice(samplekeys)
        e = decode(encrypt(encode(t),encode(keygen(t,p))))
        print("e")
        print(t)
        print(p)
        print("d")
        print(e)
        print(p)
print("q")

