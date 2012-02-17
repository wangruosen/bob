from libpybob_math import *

# add some default distance functions
import math

def euklidean_distance(x1, x2):
  """Returns the euklidean distance between the given vectors"""
  return math.sqrt(((x1-x2)*(x1-x2)).sum())


def normalized_scalar_product(x1, x2):
  """Computes the normalized scalar product (also known as the cosine between the two vectors)"""
  # Since this is actually a similarity function, we return its negative
  return 1. - numpy.dot(x1, x2) / math.sqrt(numpy.dot(x1,x1) * numpy.dot(x2,x2))


def chi_square(h1, h2):
  """Computes the chi-square distance between two histograms"""
  d = 0
  for i in range(h1.shape()[0]):
    if h1[i] != h2[i]: d += (h1[i] - h2[i])**2 / (h1[i] + h2[i])
  return d

