"""Module to generate planar graph representation.
"""

__author__ = 'Selwyn Jacob <selwynjacob90@gmail.com>'

import os
import subprocess
from markdown import markdown

def graphRep(input_seq, bracket_str):
  """ This functions requires RNAplot from the Vienna RNA Package
      It takes the input sequence and bracketed sequence to genenrate the graph in svg format.
  """
  os.system('rm ./../../rna.svg')
  proc = subprocess.Popen(['RNAplot', '-o', 'svg'], stdin=subprocess.PIPE,)
  input_str = input_seq + '\n' + bracket_str;
  proc.communicate(input_str)
  
  file = open('rna.svg', 'r')
  graph_svg = markdown(file.read())
  return graph_svg

