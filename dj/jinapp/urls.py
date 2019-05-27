from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^datachange', views.datachange, name='datachange'),
    url(r'^test', views.test, name='test'),
    url(r'^search', views.search, name='search'),
    
    #url(r'articles/<int:year>/',views.year_arc,name='art'),
]
