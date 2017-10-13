#-------------------------------------------------------------------------------
#  BubbleSort.py
#  Sorts any list whose elements are comparable
#-------------------------------------------------------------------------------

def swap(L, i, j):
   temp = L[i]
   L[i] = L[j]
   L[j] = temp
   # end of swap()

def sort(L):  # implements the Bubble Sort algorithm
   for i in range(len(L)-1,0,-1):  
      for j in range(i):
         if L[j]>L[j+1]:
            swap(L, j, j+1)
         # print(L)
      # print(L)
      # end or inner for loop
   # end or outer for loop
# out of function sort()
   
   
#-- main program --------------------------------------------------------------

#A = list(range(100,0,-1))
A = [8,2,9,3,5,-34,67]
print('\nbefore:')
print(A)
sort(A)
print('\nafter:')
print(A)
  