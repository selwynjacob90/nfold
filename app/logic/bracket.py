""" Module which generates the bracketed representation from the nussinov's sequence.
"""

__author__ = 'Selwyn Jacob <selwynjacob90@gmail.com>'


def bracketRep(seq):
  bracket_seq = []
  for i in range(0, len(seq)):
    if seq[i] == i+1:
      bracket_seq.append('.')
    else:
      if i+1 > seq[i]:
        bracket_seq.append(')')
      else: 
        bracket_seq.append('(')
  
  return bracket_seq
   
