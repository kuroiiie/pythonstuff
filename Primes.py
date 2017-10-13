#------------------------------------------------------------------------------
# Chloe Jiang
# cfjiang@ucsc.edu
# programming assignment 4
# This program asks for the user to enter how many prime numbers to find
#------------------------------------------------------------------------------

def IsPrime(m, L):
    for prime in L:
        if (m % prime == 0):
            return False
    return True

def PrimeLists(n):
    primeList = [2]
    index = 3
    while (len(primeList) < n):
        if (IsPrime(index, primeList)):
            primeList.append(index)
        index += 1
    return (primeList)

def PrintPrimes(primeList):
    for i in range(0, len(primeList)):
        print (str(primeList[i]) + " ", end= "\n" 
        	if (i != 0 and i % 10 == 0) 
        	else "")

#------------------------------------------------------------------------------

pp = int(input('\nEnter the number of primes to compute: '))
print ('\nThe first ' + str(pp) + ' primes are:')
PrintPrimes(PrimeLists(pp))