"""
URL configuration for home_work_dj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from main import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

    ОСНОВНОЕ ПРИЛОЖЕНИЕ

"""
from django.contrib import admin
from django.urls import path,include
# from my_app.views import index, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('my_app.urls',namespace='main')),
    path('catalog/',include('goods.urls',namespace='catalog'))
    # path('',index,name='index'),
    # path('about',about,name='about'),
]
