from django.conf.urls import url
from . import views          
urlpatterns = [
    # below routes are rendering templates
    url(r'^$', views.index, name='my_index'),
    url(r'^new$', views.new, name='my_new'),
    # below routes is for post/update actions for User model in db
    url(r'^create$', views.create, name='my_create'),
    url(r'^(?P<id>\d+)/update$', views.update, name='my_update'),
    # # below render individual data
    url(r'^(?P<id>\d+)/edit$', views.edit, name='my_edit'),
    url(r'^(?P<id>\d+)/destroy$', views.destroy, name='my_destroy'),
    url(r'^(?P<id>\d+)$', views.show, name='my_show')
]