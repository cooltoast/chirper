from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^tweet/(?P<tweet_id>[0-9]+)/$', views.tweet, name='tweet'),
]
