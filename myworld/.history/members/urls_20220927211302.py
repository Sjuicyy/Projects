from django.urls import path

from . import url


urlpatterns = [
    path('','views.index',name='index')
]
