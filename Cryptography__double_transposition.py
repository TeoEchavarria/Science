# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 17:36:25 2022

@author: Mateo
"""

from itertools import *

from hunspell import Hunspell
h = Hunspell()

import numpy as np


def fractioning_words(cracked_text):
  words = []
  num = len(cracked_text[::])
  for j in range(3,7):
    for i in range(num-j):
      word = cracked_text[num-1-i-j:num-i]
      if h.spell(word):
        words.append(word)
  return words

def list_text(listT):
    word = ""
    for i in listT:
        word+= i
    return word

sentence = "IAUTMDCSMNIMREBOTNELSTRHEREOAEVMWIHTSEEATMAEOHWHSYCEELTTEOHMUOUFEHTRFT"

col = 10
row = 7

array = [[ j for j in sentence[i*row:(i+1)*row]] for i in range(col)]

print(np.array(array))

permutations_row = list(permutations(array))
permutations_columns = list(permutations([i for i in range(row)]))

aux = 0
final_permutation = []

print(len(list(permutations_row)), len(list(permutations_columns)))

for p_col in permutations_columns:
    for p_row in permutations_row:
        sentence_new = ""
        for row_int in p_row:    
            sentence_new += list_text([row_int[i] for i in p_col])
        
        
        if len(fractioning_words(sentence_new)) > aux:
            aux = len(fractioning_words(sentence_new))
            final_permutation = [p_row, p_col]
            print(f"{aux}= ", sentence_new, fractioning_words(sentence_new))
            
            
print(final_permutation) 
        
