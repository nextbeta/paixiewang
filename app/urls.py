from django.conf.urls import url, include
from app import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^login.html/$', views.index_, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^cart/$', views.cart, name='cart'),
]