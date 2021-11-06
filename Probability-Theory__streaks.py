import numpy as np
import matplotlib.pyplot as plt

#m = Number of times a throw is made
#n = Number of streaks

#R refers to the number of lists in which at least one sequence of {n} consecutive 1's is obtained.
def R(m,n,d, r_previous):
  key = m * n * d
  if key in r_previous:
    return r_previous[key]

  if m == n:
    return 1
  elif m < n:
    return 0
  resultado = d*R(m-1, n, d, r_previous) + (d-1)*(d ** (m-n-1) -R(m-n-1, n, d, r_previous))
  r_previous[key] = resultado
  return resultado

#Probability of minimum streak
def P(m,n,d):
  r_previous = {}
  return R(m,n,d, r_previous)/(d**m)



#__________ GRAFICA __________

def grafic_prob(numPossibleResults, min_streak, maxPitches):
#MONEDA
  allLaunches = [i for i in range(maxPitches)]
  Probabilities= [ P(i,min_streak, numPossibleResults) for i in range(maxPitches)]

  plt.bar(allLaunches,Probabilities, color="b")
  plt.xlabel('M')
  plt.ylabel('P(M,N)')
  plt.show()

if __name__ == '__main__':
  #coin
  numPossibleResults = 2
  min_streak = 3
  #Number of pitches to achieve the streak
  fixedPitches = 10
  maxPitches = 60

  print(P(fixedPitches,min_streak,numPossibleResults))
  grafic_prob(numPossibleResults,min_streak,maxPitches)