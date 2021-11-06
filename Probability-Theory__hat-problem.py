import itertools
import random
from math import factorial

def hat_problem(num_permutations, num_items):
  # Base = The sequence in which each person has their own hat.
  # [0,1,2,3]
  # Man 0 takes hat 0, man 1 takes hat 1 ...
  base = [i for i in range(num_items)]

  #Taking into account the base which is [0,1,2,...,num_items-1] all permutations are created.
  permutations = list(itertools.permutations(base))
  #As we may take only a portion of the whole omega (num_items!) by decreasing the permutation number
  #                                      <random.shuffle> reorders all possible permutations randomly
  random.shuffle(permutations)
  counter = 0
  for permutation in permutations[:num_permutations]:
    i = 0
    while i < num_items:
      #If the element within the permutation is in the same position as the base = It has its own hat.
      if permutation.index(permutation[i]) == base.index(permutation[i]):
        counter += 1
        #That's enough for me for that permutation to be valid, so don't try the others.
        i = num_items
      else:
        i += 1
  
  return (1 - counter/len(permutations[:num_permutations]))

if __name__ == '__main__':
  print('take all values put <-1> \n')
  num_permutations = int(input('Number of permutations: '))
  num_items = int(input('Number of items: '))  

  #If num_permutations equals -1, take all permutations which equals "num_items!"
  if num_permutations == -1:
    num_permutations = factorial(num_items)



