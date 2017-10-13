#-------------------------------------------------------------------------------
#  Collatz3.py
#-------------------------------------------------------------------------------

def oddPart(n):
   """ returns the largest odd number dividing n """
   if n%2==1:
      return n;
   else:
      return oddPart(n//2)
   # end oddPart()

def abreviatedCollatz(n, L):
   while n != 1:
      L.append(n)
      if n % 2 == 0:        # n is even
         n = oddPart(n)
      else:                 # n is odd
         n = 3*n + 1
   L.append(n)
   # end abreviatedCollatz()


#-- main program --------------------------------------------------------------

k = int(input('Enter an integer: '))
C = []
abreviatedCollatz(k, C)
print('The Abreviated Collatz sequence starting at', k, 'is:')
print(C)