from django.conf.urls import url, include
from .views import products, training, manuals, templates, audit

urlpatterns = [
    url(r'^products/$', products, name='products'),
    url(r'^training/$', training, name='training'),
    url(r'^manuals/$', manuals, name='manuals'),
    url(r'^templates/$', templates, name='templates'),
    url(r'^audit/$', audit, name='audit'),
]