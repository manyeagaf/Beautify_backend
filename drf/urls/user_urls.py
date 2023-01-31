from drf.views import user_views
from django.urls import path

urlpatterns = [
    path('login/',user_views.MyTokenObtainPairView.as_view(),name='token-obtain-pair'),
    path('all/', user_views.AllUsers.as_view(), name='users'),
    path('create/', user_views.CustomUserCreate.as_view(), name='user-regeister'),
    path('current-user/', user_views.CurrentUser.as_view(), name='current-user'),
]
