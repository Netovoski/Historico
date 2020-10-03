from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^hist_2015_1$', Hist_2015_1, name="historico_2015"),
    url(r'^hist_2015_2$', Hist_2015_2, name="historico_2015_2"),
    url(r'^hist_2015_3$', Hist_2015_3, name="historico_2015_3"),
    url(r'^hist_2015_4$', Hist_2015_4, name="historico_2015_4"),
    url(r'^hist_2015_5$', Hist_2015_5, name="historico_2015_5"),
    url(r'^hist_2015_6$', Hist_2015_6, name="historico_2015_6"),
    url(r'^hist_2015_7$', Hist_2015_7, name="historico_2015_7"),
    url(r'^hist_2015_8$', Hist_2015_8, name="historico_2015_8"),
    url(r'^hist_2015_9$', Hist_2015_9, name="historico_2015_9"),
    url(r'^hist_2015_10$', Hist_2015_10, name="historico_2015_10"),
    url(r'^hist_2015_11$', Hist_2015_11, name="historico_2015_11"),
    url(r'^hist_2015_12$', Hist_2015_12, name="historico_2015_12"),
    url(r'^hist_2016_1$', Hist_2016_1, name="historico_2016"),
    url(r'^hist_2016_2$', Hist_2016_2, name="historico_2016_2"),
    url(r'^hist_2016_3$', Hist_2016_3, name="historico_2016_3"),
    url(r'^hist_2017_1$', Hist_2017_1, name="historico_2017"),
]

