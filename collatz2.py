#-------------------------------------------------------------------------------
#  Collatz2.py
#-------------------------------------------------------------------------------

def oddPart(n):
   """ returns the largest odd number dividing n """
   if n%2==1:
      return n;
   else:
      return oddPart(n//2)  # recursive call to oddPart()
   # end oddPart()
      
def abreviatedCollatz(n):
   """ 
   prints the Collatz sub-sequence obtained by dividing out all even factors 
   in a single step
   """
   while n != 1:
      print(n, end=", ")
      if n % 2 == 0:        # n is even
         n = oddPart(n)
      else:                 # n is odd
         n = 3*n + 1
   print(n, end=".\n")
   #end abreviatedCollatz()
   
#-- main program --------------------------------------------------------------

k = int(input('Enter an integer: '))
print('The Abreviated Collatz sequence starting at', k, 'is:')
abreviatedCollatz(k)