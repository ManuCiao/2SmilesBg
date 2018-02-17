from django.conf.urls import url
from django.conf import settings
from .feeds import LatestPostsFeed
from . import views
from . import models

urlpatterns = [
    # post views
    url(r'^$', views.post_list, name='post_list'),
    url(r'^tag/(?P<tag_slug>[-\w]+)/$', views.post_list, name='post_list_by_tag'),
    #url(r'^$', views.PostListView.as_view(), name='post_list'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
        views.post_detail,
        name='post_detail'),
    #url(r'^month/(\d+)/(\d+)/$', views.month, name='month'),
    url(r'^(?P<year>\d{4})/$', views.year_archive, name='year_archive'),
    url(r'^(?P<year>\d{4})/(?P<month>\d+)/$', views.month, name='month'),
    url(r'^(?P<post_id>\d+)/share/$', views.post_share, name='post_share'),
    url(r'^feed/$', LatestPostsFeed(), name='post_feed'),
    url(r'^search/$', views.post_search, name='post_search'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
]
