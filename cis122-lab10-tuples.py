'''
CIS 122 Fall 2021
Author: Liam Bouffard
Partner: Andrew
Objective: create a function that accepts a variable length
     number of arguments of numbers. The function will return 
     the number of arguments, minimum value, maximum value, mean \
     and median as a tuple.
'''

# cis122-lab10-data.txt
def number_stats(*args):
   '''
   retrieves the stats of the list numebrs
   '''
   total = 0
   median = 0
   mean = 0
   max_val = 0
   min_val = -1
   for i in args:
      total += i
      if i > max_val:
         max_val = i
      if min_val == -1 or i < min_val:
         min_val = i

   if len(args) > 0:
      mean = total / len(args)

      t = sorted(args) # Returns sorted list
      print(t)

      if len(t) == 1:
         median = args[0]
      elif len(t) % 2 == 0:
         pos1 = (len(t) // 2)
         pos2 = (len(t) // 2) - 1
         median = (t[pos1] + t[pos2]) / 2
      else:
         median = t[len(t) // 2]


   return len(args), min_val, max_val, mean, median

fin = input("Enter the name of a file: ")
file = open(fin).readlines()
stripped = tuple([int(item.strip()) for item in file])

data = stripped
count, minv, maxv, mean, median = number_stats(*data)
print("Count:", count)
print("Min:", minv)
print("Max:", maxv)
print("Mean:", mean)
print("Median:", median)
