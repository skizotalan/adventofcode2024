import helpers.config as cfg

def get_d1_1():
  d1_input = cfg.d1_input

  # Split the data into lines
  lines = d1_input.strip().split('\n')

  # Initialize two empty arrays
  array1 = []
  array2 = []

  # Iterate over each line and split the numbers
  for line in lines:
      num1, num2 = map(int, line.split())
      array1.append(num1)
      array2.append(num2)

  # sort the arrays
  array1.sort()
  array2.sort()

  # combine the arrays into a dictionary w/ a difference column
  combined_dict = {
    'Array1': array1,
    'Array2': array2,
    'AbsoluteDifference': [abs(a - b) for a, b in zip(array1, array2)]
  }

  # calculate the total absolute difference
  total_absolute_difference = sum(combined_dict['AbsoluteDifference'])
  return(total_absolute_difference)