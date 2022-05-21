from django.urls import path

from .views import OffersView

app_name = "offers"

urlpatterns = [

    path("offers/", OffersView.as_view(), name="offers"),
]
