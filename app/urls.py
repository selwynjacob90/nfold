from django.conf.urls.defaults import patterns, include, url

from app.views import RnaInput, DisplayRepresentations 


urlpatterns = patterns('',
                       url(r'^new/$',
                           RnaInput,
                           name = 'input_page'), 

                       url(r'^(?P<object_id>\d+)/$',
                           DisplayRepresentations,
                           name = 'display_rep'),

                      )
