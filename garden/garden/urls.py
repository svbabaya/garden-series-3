"""
URL configuration for garden project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import set_language
from . import views

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path("", views.index, name="index"),
    path("index", views.index, name="index"),
    path("home", views.index, name="index")
]

# urlpatterns += i18n_patterns(
#     path('', include('yourapp.urls'))
# )
