from django.urls import path
from . import views

app_name = 'urls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:key>', views.redirectTo, name='redirectTo'),
    path('shorted/<int:num>', views.shorted, name='shorted'),
]