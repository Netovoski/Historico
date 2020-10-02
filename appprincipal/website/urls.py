from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^hist_2015_1$', Hist_2015_1, name="historico_2015"),
    url(r'^hist_2015_2$', Hist_2015_2, name="historico_2015_2"),
    url(r'^hist_2015_3$', Hist_2015_3, name="historico_2015_3"),
    url(r'^hist_2016_1$', Hist_2016_1, name="historico_2016"),
    url(r'^hist_2016_2$', Hist_2016_2, name="historico_2016_2"),
    url(r'^hist_2016_3$', Hist_2016_3, name="historico_2016_3"),
    url(r'^hist_2017_1$', Hist_2017_1, name="historico_2017"),
]

