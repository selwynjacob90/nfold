""" Module containing the implementation of Nussinov's algorithm which builds the nussinov's sequence.
"""

__author__ = 'Selwyn Jacob <selwynjacob90@gmail.com>'

import sys
import string
import numpy as np 


def delta(a,b):
  """ Returns 1 if they are base-pairs, else returns 0.

  """
  delta = 0

  if a == 'A' and b == 'U':
    return 1

  elif a == 'U' and b == 'A':
    return 1

  elif a == 'G' and b == 'C':
    return 1

  elif a == 'C' and b == 'G':
    return 1

  elif a == 'G' and b == 'U':
    return 1

  elif a == 'U' and b == 'G':
    return 1

  else:
    return 0;


def matrixFill(sequence):
  """Fills the matrix using the four Nussinov's equations.

  """
  L = len(sequence)
  matrix = np.zeros((L,L))

  for n in xrange(1,L):
    for j in xrange(n,L):
      i = j-n
      case1 = matrix[i+1,j-1] + delta(sequence[i],sequence[j])
      case2 = matrix[i+1,j]
      case3 = matrix[i,j-1]

      if i+3 <= j:

        tmp=[]
        for k in xrange(i+1,j):
	     tmp.append(matrix[i,k] + matrix[k+1,j])

        case4=max(tmp)
        matrix[i,j]=max(case1,case2,case3,case4)

      else:

         matrix[i,j]=max(case1,case2,case3)

  return matrix



def traceback(matrix,sequence,i,j,sq):

  """This function traces back the optimal structure from the generated Matrix.

     Arguments:

        matrix : matrix generated in the matrixFill step

        seuquence: The given rna sequence

        i, j : Current positions in the matrix

        sq: The resultant sequence
  """
  if i<j:
    if matrix[i,j] == matrix[i+1,j]:
      traceback(matrix, sequence, i+1, j, sq)
      sq[i] = i+1
    
    elif matrix[i,j]== matrix[i,j-1]:
      traceback(matrix, sequence, i, j-1, sq)
      sq[j] = j+1 

    elif matrix[i,j] == matrix[i+1,j-1] + delta(sequence[i],sequence[j]):
      sq[i] = j+1
      sq[j] = i+1
      traceback(matrix, sequence, i+1, j-1, sq)

    else:
      for k in xrange(i+1,j):

        if matrix[i,j] == matrix[i,k] + matrix[k+1,j]:
          traceback(matrix, sequence , i, k, sq)
          traceback(matrix,sequence , k+1, j, sq)
          break

  return sq

def buildSequence(seq):
   """ This function is the starting point of Nussinov's algorithm.
       It takes the raw sequence and builds the nussinov's sequence calling
       the above two methods - matrixFill and traceback
   """

   sequence = []
   output_seq = []
   sequence.append(seq) 
    
   for q in xrange(0,len(sequence)):
	sq = np.zeros(len(sequence[0]))
        sq = traceback(matrixFill(sequence[q]),sequence[q],0,len(sequence[q])-1,sq)
   for i in xrange(0,len(sq)):
       output_seq.append(int(sq[i]))
   return output_seq
