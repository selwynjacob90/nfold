""" Models for the app.
"""

__author__ = 'Selwyn Jacob <selwynjacob90@gmail.com>'

from django.db import models

class Sequence(models.Model):
  """ Model to hold the rna sequence.
  """
  title = models.CharField(max_length=50)
  raw_seq = models.TextField()
  output_seq = models.CommaSeparatedIntegerField(max_length=500)
  bracketed_str = models.TextField()
  graph_svg = models.TextField()
  

  def __unicode__(self):
     return self.title

  def get_absolute_url(self):
     return "/nfold/%s/" %self.id
