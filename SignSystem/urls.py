"""SignSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,re_path
import xadmin
from login import views

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('login',views.login_action),
    path('Message_event',views.message_event),
    re_path(r'^search_name$',views.Search_name),
    re_path(r'^Guest_manage',views.Guest_manage),
    re_path(r'^sign_index-(?P<event_id>[0-9]+)$',views.sign_index),
    re_path(r'^sign_index_action-(?P<event_id>[0-9]+)$',views.sign_index_action)
]
