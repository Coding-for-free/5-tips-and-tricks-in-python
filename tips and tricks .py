# 1. “Else” condition inside a “for” loop

numbers = [2, 4, 6, 8, 1]

for number in numbers:
    if number % 2 == 1:
        print(number)
        break
else:
    print("No odd numbers ")





# 2. Get n largest or n smallest elements in a list using the module heapq

import heapq

scores = [52, 34, 65, 88, 92, 76, 16, 50, 34, 83]

print(heapq.nlargest(3, scores))  # [92, 88, 83]
print(heapq.nsmallest(5, scores))  # [16, 34, 34, 50, 52]




# 3. Get all the elements in the middle of the list



_, *elements_in_the_middle, _ = [1, 2, 3, 4, 5, 6, 7, 8]
print(elements_in_the_middle)  # [2, 3, 4, 5, 6, 7]




#4. Assign multiple variables in just one line

one, two, three, four = 1, 2, 3, 4





# 5.Repeat strings without looping

string = "Abc"

print(string * 5)



