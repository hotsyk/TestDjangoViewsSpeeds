from django.conf.urls.defaults import *

urlpatterns = patterns('testapp.views',
        (r'^function_based_view/$', 'function_based_view'),
        (r'^class_based_view/$', 'class_based_views'),
)
