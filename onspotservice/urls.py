"""onspotservice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from userside import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_jwt.views import refresh_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('userside.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('refresh-token/', refresh_jwt_token),
    path('rest-auth/', include('rest_framework.urls')),
    path('', include('django.contrib.auth.urls')),

    #path('vehicles/', views.VehicleList),
]

#urlpatterns = format_suffix_patterns(urlpatterns)