from django.conf.urls.defaults import patterns, include, url

from app.models import Sequence
from app.views import RnaInput 


urlpatterns = patterns('',
                       url(r'^new/$',
                           RnaInput,
                           name = 'input_page'), 
                      )
