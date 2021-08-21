import asyncio
import json

from django.shortcuts import render

# Create your views here.
from django.views import generic

from api_v1.async_requests import get_address_all


class HomeView(generic.TemplateView):
    """

    """
    template_name = 'front/base.html'

    def get_context_data(self, **kwargs):
        keyword = '서울 중구'
        address_number = 5
        context = super(HomeView, self).get_context_data(**kwargs)
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        ko, en = asyncio.run(get_address_all(keyword, address_number))
        ko_list = json.loads(ko)['results']['juso']
        en_list = json.loads(en)['results']['juso']
        data = []
        for ko_str, en_str in zip(ko_list, en_list):
            new_dict = {
                "ko_jibunAddr": ko_str.get('jibunAddr', ''),
                "ko_roadAddr": ko_str.get('roadAddr', ''),
                "en_jibunAddr": en_str.get('jibunAddr', ''),
                "en_roadAddr": en_str.get('roadAddr', '')
            }
            data.append(new_dict)
        print(data)
        return context

