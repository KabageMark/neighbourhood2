from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns=[
    url(r'^$',views.home,name = 'home'),
    url(r'^profile$', views.Profiles, name='profile'),
    url(r'^business$', views.business, name='business'),
    url(r'^search$', views.search_results, name='search'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)