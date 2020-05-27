from django.urls import path
from .views import home, addFact

urlpatterns = [
    path('', home, name='homepage'),
    path('add', addFact, name='addFact')
]