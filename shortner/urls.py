from django.urls import path
from .views import form_view,get_view

urlpatterns = [
   path('<str:short_link>/', get_view, name='get_view'),
   path('',form_view, name='home'), 
]