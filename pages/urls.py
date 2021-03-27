from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='foods'),
    path('prato/<slug:slug_text>', views.listing, name='listing'), #<int:listing_id> <slug:slug_text> name='listing'
    path('pesquisa', views.search, name='search'),
]