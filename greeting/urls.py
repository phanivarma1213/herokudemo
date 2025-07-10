from django.urls import path
from .views import GreetingView

urlpatterns = [
    path('greet/', GreetingView.as_view()),
]