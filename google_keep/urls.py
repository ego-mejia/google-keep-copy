from django.urls import path
from .views import note_list

urlpatterns = [
    path('', note_list, name='note_list'), # '' represents the base url on the app, the index.
]