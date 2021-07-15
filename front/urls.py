from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from django.conf import urls

# urls.handler404 = 'v2_front_base.views.handler404'
# urls.handler500 = 'v2_front_base.views.handler500'
from front import views

app_name = 'front'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),

]
