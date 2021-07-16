import asyncio
import json

from django.shortcuts import render

# Create your views here.
from django.views import generic

from api_v1.async_requests import address_main


class HomeView(generic.TemplateView):
    template_name = 'front/base.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        ko, en = asyncio.run(address_main("안양 908"))
        return context

