'''
CIS 122 Fall 2021
Author: Liam Bouffard
Objective: data analysis
'''

import random

def get_random_integer_list(num, start_range = 1, end_range = 100, sort_list = 'N'):
  '''
  guardian code for num must be integer and above 0
  loop over parameter integer
  assign var r to a radnom num between the start and end range for every num iteration
  add r to a list
  '''
  # intialize t to an empty string
  t = []
  # guardian code for num must be integer and greater/equal to zero

  if num <= 0:
    print('num must be > 0')
  elif not isinstance(num, int):
    print('num must be an integer')
  elif not isinstance(start_range, int) or not isinstance(end_range, int):
    print('start_range and end_range must be integers')
  # assign var r to a radnom num between the start and end range for every num iteration 
  #   add r to a list
  else:
    for i in range(num):
      r = random.randint(start_range, end_range)
      t.append(r)
  # if sort_list parameter equals Y then sort list in numrical order
    if sort_list.upper() == 'Y':
      t.sort()

  return t

t = get_random_integer_list(100, sort_list = 'Y')

#----------------------------------------------------------
# done
def get_high_score(t):
  '''
  retrieves highest score from list
  '''
  if isinstance(t, list):
    is_list = True
  else:
    print('List argument expected')
    return(-1)
  if t == []:
    return(0)
  copy_t = sorted(t[:])
  return (copy_t[(len(copy_t) - 1)])

# ---------------------------------------------------------
# done
def get_low_score(t):
  '''
  retrieves lowest score from list
  '''
  if isinstance(t, list):
    is_list = True
  else:
    print('List argument expected')
    return(-1)
  if t == []:
    return(0)
  copy_t = sorted(t[:])
  return (copy_t[0])

# ---------------------------------------------------------
# done
def get_mean_score(t):
  '''
  returns mean score of list
  '''
  if isinstance(t, list):
    is_list = True
  else:
    print('List argument expected')
    return(-1)
  if t == []:
    return(0)
  mean_score = sum(t) / ((len(t) + 1))
  return mean_score

# ---------------------------------------------------------
# done
def get_median_score(t):
  # guardian code
  if isinstance(t, list):
    is_list = True
  else:
    print('List argument expected')
    return(-1)
  if t == []:
    return(0)
  # middle num -
  middle_num = len(t) / 2
  if (len(t) % 2) == 0: # (even)
    lower_val = int((middle_num) - 1)
    upper_val = int((middle_num))
    median = (t[lower_val] + t[upper_val]) / 2
  else: # (odd)
    len_num = int((middle_num + 0.5) - 1)
    median = t[len_num]
  return median

# ---------------------------------------------------------
# done
def count_range(t, start, end):
  '''
  count the number of scores within a low and high range
  '''
  if not isinstance(t, list):
    print('List argument expected')
    return (-1)

  elif not isinstance(start, int) and isinstance(end, int):
    print('Start and end must be integers')
    return(-1)

  elif (start > end) or (start == end):
    print ('start must be < end')
    return (-1)

  elif t == []:
    return (0)

  else:
    counter = 0
    for i in t:
      if start <= i <= end:
        counter += 1
      else:
        pass
  
  return counter

# ----------------------------------------------------------
# done
def list_range(t):
  print ('A -', count_range(t, 90, 100))
  print ('B -',count_range(t, 80, 89))
  print ('C -',count_range(t, 70, 79))
  print ('D -',count_range(t, 60, 69))
  print ('F -',count_range(t, 0, 60))

list_range(t)