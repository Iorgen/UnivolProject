from django.http.response import HttpResponseBase
from django.shortcuts import render, redirect

# Create your views here.

from api_volunteers_search_supporter.vk_searcher.vk_user_fetcher import VKUserFetcher


def get_prediction_by_keyword_and_city(response):
    if response.method == 'POST':
        keyword = response.POST.get('keyword')
        city_id = response.POST.get('city')

        if keyword is None:
            return redirect('/')

        fetcher = VKUserFetcher()
        users = fetcher.get_result_volunteers_from_vk(keyword, city_id)
        vk_url = 'http://vk.com/id'
        context = {
            'users_urls': [vk_url + str(user) for user in users],
        }
        return render(response, 'univol/predicted_users.html', context)


def get_vk_prediction_page(response):
    if response.method == 'GET':
        return render(response, 'univol/vk_fetch_settings.html')
