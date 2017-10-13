#------------------------------------------------------------------------------
# Chloe Jiang
# cfjiang@ucsc.edu
# programming assignment 6
# Rolls N number of dice of M sides to get stastics of their sum
#------------------------------------------------------------------------------

import random
rnd = random.Random(237)

n = int(input("\nEnter the number of dice: "))
while n < 1:
    print("The number of dice must be at least 1")
    n = int(input("Please enter the number of dice: "))


m = int(input("\nEnter the number of sides on each dice: "))
while m < 2:
    print("The number of sides on each dice must be at least 2")
    m = int(input("Please enter the number of sides on each die: "))


t = int(input("\nEnter the number of trials to perform: "))
while t < 1:
    print("The number of trials to perform must be at least 1")
    t = int(input("Please enter the number of trials to perform: "))


mn = n
mx = n*m

frequency = [0]*(mx+1)
relativefreq = [0]*(mx+1)
experimentprob = [0]*(mx+1)


def throwDice(m, n):
    lists = []
    for i in range(n):
        lists.append(rnd.randrange(1, m+1))
    tuple(lists)
    return lists

for i in range(t):
    T = throwDice(m, n)
    sumall = 0
    for j in range(len(T)):
        sumall += T[j]
    frequency[sumall] += 1

for i in range(mn, len(frequency)):
    relativefreq[i] = frequency[i]/t
    experimentprob[i] = relativefreq[i]*100


l1 = "{0:<8}{1:<14}{2:<24}{3:<20}"
l2 = 70*"-"
l3 = "{0:>3}{1:>11.0f}{2:>19.5f}{3:>22.2f} %"
print(l1.format(" Sum","Frequency","Relative Frequency","Experimental Probability"))
print(l2)
for i in range(mn, len(frequency)):
    print(l3.format(i, frequency[i], relativefreq[i], experimentprob[i]))
print()