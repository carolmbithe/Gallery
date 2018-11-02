from django.conf.urls import url
from . import views


urlpatterns=[
    url('^$',views.index,name='index'),
    url('^today/$',views.today_photos,name='photosToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_photos,name = 'pastPhotos'),
    url(r'^search/',views.search_results,name='search_results'),
]
