from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^mark/$', views.add_mark, name='add_mark'),
    url(r'^marks/$', views.get_marks, name='get_marks'),
    url(r'^$', views.index, name='index'),
]
