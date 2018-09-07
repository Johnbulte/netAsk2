

from django.conf.urls import url
from .views import *



urlpatterns=[
url(r'^$',login_views,name='login'),
url(r'^reg/$',register_views,name='reg'),
url(r'^system/$',system_views,name='sys'),
url(r'^qa/$',qa_views),
url(r'^aqu/$',aq_views),
url(r'^dati/$',dati_views),
url(r'^paihan/$',paihan_views),

]