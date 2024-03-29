"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from user.views import FacebookLogin,GithubLogin,GoogleLogin

urlpatterns = [
    path('',include('home.urls')),
    path('admin/', admin.site.urls),
    path('api/products/', include('drf.urls.product_urls')),
    path('api/orders/', include('drf.urls.order_urls')),
    path('api/users/', include('drf.urls.user_urls')),
    path('api-auth/', include('rest_framework.urls')),



    #dj-rest-auth for social
    path('dj-rest-auth/', include('dj_rest_auth.urls')), 
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('dj-rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('dj-rest-auth/github/', GithubLogin.as_view(), name='github_login'),
    path('dj-rest-auth/google/', GoogleLogin.as_view(), name='google_login')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
