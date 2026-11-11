import numpy as np


def normalize_numbers(arr):
  """
  Normalize a two-dimensional array by its largest value.

  >>> normalize_numbers(np.array([[1,2,3,4],[5,6,7,8]]))
  array([[0.125, 0.25, 0.375, 0.5],[0.625, 0.75, 0.875, 1.]])
  """
  return arr / np.max(arr)
