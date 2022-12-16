def sum_the_numbers (*args):              # define our function
  total = 0                               # set initial total to zero
  for num in args:                        # loop through each value
    total += num                          # add each value to the total
    return total                          # return the summed total
  
summation = sum_the_numbers(5, 10)        # execute our function
print(summation)                          # print the total