from django.urls import path

from .views import HomeView, OffersView

app_name = "offers"

urlpatterns = [

    path("", HomeView.as_view(), name="home"),
    path("offers/", OffersView.as_view(), name="offers"),
]
