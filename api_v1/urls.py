from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from django.conf import urls
from . import views
# urls.handler404 = 'v2_front_base.views.handler404'
# urls.handler500 = 'v2_front_base.views.handler500'


app_name = 'api_v1'

urlpatterns = [
    # path('', views.HomeView.as_view(), name='home'),

]
