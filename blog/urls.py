"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.urls import path , include
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from account.api import UserViewSet

router = DefaultRouter()
router.register('user',UserViewSet)


from account.views import (
    RegisteritionView,
    LoginView,
    LogoutView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myblog.urls')),
    path('api-auth/',include('rest_framework.urls')),
    path('api/',include('myblog.APIUrls')),
    path('api/',include(router.urls)),
    path('register/', RegisteritionView.as_view(), name='register-url' ),
    path('login/' , LoginView.as_view(), name = 'login-url'),
    path('logout/', LogoutView.as_view(), name= 'logout-url'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
     document_root=settings.MEDIA_ROOT)

