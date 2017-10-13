#------------------------------------------------------------------------------
#  ReverseList.py
#------------------------------------------------------------------------------

def swap(T, i, j):
   """ swap elements T[i] and T[j] in list T """
   temp = T[i]
   T[i] = T[j]
   T[j] = temp
# end swap()

def reverse_list(T):
   """ reverse the list T """
   i = 0
   j = len(T)-1
   while i<j:
      swap(T, i, j)
      i += 1
      j -= 1
   # end while
# end reverse_list()	  

 
#-- main program --------------------------------------------------------------

L = [1,2,3,4,5]
print(L)
reverse_list(L)
print(L)
