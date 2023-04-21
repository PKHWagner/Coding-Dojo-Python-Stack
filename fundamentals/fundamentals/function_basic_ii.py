# Countdown
def countdown(x):
  output = []
  for i in range(x,-1,-1):
    output.append(i)
  return output
print(countdown(10))

# Print and Return
def print_return(some_list):
  print(some_list[0])
  return some_list[1]
print(print_return([3,34]))

# First Plus Length
def sum_first_plus_length(some_list):
  return some_list[0] + len(some_list)
print(sum_first_plus_length([300,234,543,555,697,999,10002]))

# Values Greater Than Second
def values_greater_than_second(some_list):
  if len(some_list) < 2:
    return False
  output = []
  for i in range(0,len(some_list)):
    if some_list[i] > some_list[1]:
      output.append(some_list[i])
  print(len(output))
  return output
print(values_greater_than_second([4,3,1,5,8,0,6,2,9]))
print(values_greater_than_second([7]))

# This Length, That Value
def length_value(x,y):
  output = []
  for i in range(0,x):
    output.append(y)
  return output
print(length_value(7,11))
print(length_value(11,7))