#------------------------------------------------------------------------------
# BinarySearch.py
#------------------------------------------------------------------------------

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
   # end of sort()

def BinSearch(x, L):
   left = 0
   right = len(L)-1
   while left<=right:   # search space is not empty
      m = (left+right)//2
      if x == L[m]:
         return m
      elif x < L[m]:
         right = m-1
      else:  #  L[m] < x 
         left = m+1
   # if this line is reached, None is returned
   # end of BinSearch()


#-- main program --------------------------------------------------------------

target = 'seven'
words = ['one','two','three','four','five','six','seven','eight','nine','ten']

print(words)
sort(words)
print(words)
position = BinSearch(target, words)
print(target, 'found at position', position)