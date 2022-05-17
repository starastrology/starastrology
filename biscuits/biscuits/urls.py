from django.conf.urls import url
from django.urls import path
from need_this import views

urlpatterns = [
    url(r'^natal$', views.B, name='b'),
    url(r'^estimate', views.do_some_stuff, name='estimate'),
    path('', views.Splash, name='splash'),
    path('celebrity/<int:zodiac_value>', views.Individuals, name='individuals'),
    path('calculator', views.Calculator, name='calculator'),
    path('calculate', views.Calculate, name='calculate')
]
