# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 17:09:09 2022

@author: Mateo
"""

from english_words import english_words_set

# ----- auxiliary functions -----

adecedary = "abcdefghijklmnopqrstuvwxyz"
adecedary_c = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def scroll(word, key):
  cracked_text = word
  for i in range(26):
    cracked_text = cracked_text.replace(adecedary_c[i], adecedary[(i - key) % 26])
  return  cracked_text

def check_words(word):
  if word in english_words_set:
    return True
  return False

def fractioning_words(cracked_text):
  words = []
  num = len(cracked_text[::])
  for j in range(4,7):
    for i in range(num-j):
      word = cracked_text[num-1-i-j:num-1-i]
      if check_words(word):
        words.append(word)
  return words


# ----- ataque -----
key_sike = 3
coded_text = "CTMYR DOIBS RESRR RIJYR EBYLD IYMLC CYQXS RRMLQ FSDXF OWFKT CYJRR IQZSM X"
text_without_spacing = coded_text.replace(" ", "")
cut_text = []
for j in range(key_sike):
  sentence = ""
  for i in range(len(text_without_spacing)//key_sike):
    sentence += text_without_spacing[(i*key_sike)+j]

  cut_text.append(sentence)

aux = 0

for i in range(26):
  int_1 = scroll(cut_text[0], i)
  for j in range(26):
    int_2 = scroll(cut_text[1], j)
    for k in range(26):
      int_3 = scroll(cut_text[2], k)

      key = [i,j,k]

      final = ""
      for t in range(20):
        final += f"{int_1[t]}{int_2[t]}{int_3[t]}"
      
      num = len(fractioning_words(final))
      if num > aux:
        print(final, num, key)
        aux = num

