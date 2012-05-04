""" This module contains the app specific URLs
"""

__author__ = 'Selwyn Jacob <selwynjacob@gmail.com>' 

from django.conf.urls.defaults import patterns, include, url
from django.views.generic.list_detail import object_list

from app.models import Sequence
from app.views import input_page, seq_process, home, list_page, ref_page

seq_info = {'queryset' : Sequence.objects.all }

urlpatterns = patterns('',
                       url(r'^$',
                           home,
                           name = 'homepage'),
                       
                       url(r'^(?P<object_id>\d+)/$',
                           seq_process,
                           name = 'seq_detail'),

                       url(r'^new/$',
                           input_page,
                           name = 'input_page'),
           
                       url(r'^list/$',
                           list_page,
                           name = 'list_page'), 
             
                       url(r'^references/$',
                           ref_page,
                           name = 'reference_page'),
                      )
