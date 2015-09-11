n = int(input("I will estimate pi. How many terms should I use? "))
sigfigs = int(input("How many decimal places should I use in the result? "))
pi = 4*sum([((-1)**k)/(2.0*k+1) for k in range(0,n)])
print("The approximate value of pi is {0:.{1}f}".format(pi,sigfigs))
