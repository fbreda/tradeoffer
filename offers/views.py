# from django.shortcuts import render
from django.views.generic import TemplateView


class OffersView(TemplateView):
    template_name = "offers/offerslist.html"
