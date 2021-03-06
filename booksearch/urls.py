from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^about/$', views.about),
    path('search', views.search, name='search'),
    path('mylists', views.mylists, name='mylists'),
    path('signout', views.signout, name='signout'),
    path('add/', views.addition, name='add'),
    url(r'^auth/', include('social_django.urls', namespace='social')),
    path('', views.index, name='index')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
              static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
