"""URLS that apply to the entire site"""

from django.conf.urls import include, url
# from django.contrib import admin
from lists import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', views.home_page, name='home'),
    url(r'^lists/', include('lists.urls')),
]
