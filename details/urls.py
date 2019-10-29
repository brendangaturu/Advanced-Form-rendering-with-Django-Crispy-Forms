from django.urls import path
from .views import DetailView


urlpatterns = [
    path('details/', DetailView.as_view(), name='details')
]