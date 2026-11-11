
def print_line_sums(path):
  """Print the sum of the comma-separated numbers on each line.

  >>> f = open("test_numbers.csv", "w")
  >>> amount = f.write("1,2,3\\n4.5,5.5\\n")
  >>> f.close()
  >>> print_line_sums("test_numbers.csv")
  6.0
  10.0
  >>> import os
  >>> os.remove("test_numbers.csv")
  """
  f = open(path, "r")

  for line in f:
    if line.strip():
      numbers = [float(value) for value in line.split(",")]
      print(sum(numbers))

  f.close()
