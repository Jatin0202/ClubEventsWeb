from django.urls import path, re_path, include
from . import views

urlpatterns = [
    re_path(r'(?P<club_name>[\w.@+-]+)/quick$', views.club_posts, name="club"),
    re_path(r'(?P<club_name>[\w.@+-]+)/$', views.post_scraping, name="club_scrape"),
]