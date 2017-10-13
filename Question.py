#------------------------------------------------------------------------------
# Chloe Jiang
# cfjiang@ucsc.edu
# programming assignment 5
# This program plays a guessing game with the user through series of questions.
#------------------------------------------------------------------------------

print("\nEnter two numbers, low then high")
while True:
    low = int(input("low = "))
    high = int(input("high = "))
    mid = int(((low) + (high))//2)
    if (high <= low):
        print("\nPlease enter the smaller followed by the larger number")
    else:
        break
        print("\nThink of a number in the range of " + str(low) + " and " + str(high))

count = 0

while True:
    print("\nIs your number Less than, Greater than, or Equal " + str(mid) + "?")
    answer = input("Type 'L', 'G', or 'E': ")
    
    if (answer == str("L") or answer == str("l")):
        count += 1
        high = mid
        mid = int(((low) + (high))//2)
        if(low == high):
            break
    
    if (answer == str("G") or answer == str("g")):
        count += 1
        low = mid
        mid = int(((low) + (high))//2)
        if (low == high):
            break

    if (answer == str("E") or answer == str("e")):
        count += 1
        break
    
    if (low == mid or high == mid):
        print("\nYour answers have not been consistent.")
        quit()
    

if (count != 1):
   print("\nYour number is "+ str(mid) + ". I found your number in " + str(count) + " guesses.")
if (count == 1):
   print("\nI found your number in " + str(count) + " guess.")