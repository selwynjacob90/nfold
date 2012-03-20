from django.db import models

class Sequence(models.Model):
  title = models.CharField(max_length=50)
  raw_seq = models.TextField()
  output_seq = models.CommaSeparatedIntegerField(max_length=500)
  bracketed_str = models.TextField()
  graph_svg = models.TextField()
  

  def __unicode__(self):
     return self.title

  def get_absolute_url(self):
     return "/rnavis/%s/" %self.id
