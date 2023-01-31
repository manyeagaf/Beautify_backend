from django.urls import path
from drf.views import album_views

urlpatterns = [
    path('all/', album_views.AlbumList.as_view(), name='albums'),
]
