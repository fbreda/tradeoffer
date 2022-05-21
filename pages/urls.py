from django.urls import path

from .views import FaqsView, HomeView, ObjectiveView, PrivacyView

app_name = "pages"

urlpatterns = [

    path("", HomeView.as_view(), name="home"),
    path("faqs/", FaqsView.as_view(), name="faqs"),
    path("objective/", ObjectiveView.as_view(), name="objetive"),
    path("faqs/", PrivacyView.as_view(), name="privacy"),
]
