from django.urls import path
from .views import sync_from_salesforce

urlpatterns = [
    path('sf_sync/', sync_from_salesforce),
]