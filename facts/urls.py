from django.urls import path
from .views import home, addFact, morefacts

urlpatterns = [
    path('', home, name='homepage'),
    path('add', addFact, name='addFact'),
    path('facts', morefacts, name='morefacts'),
]