from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='foods'),
    path('prato/<slug:slug_text>', views.listing, name='listing'), #<int:listing_id> <slug:slug_text> name='listing'
    path('<slug:slug_text>/update/', food_update_view, name='food-update'),
    path('<slug:slug_text>/delete/', food_delete_view, name='food-delete'),
    path('pesquisa', views.search, name='search'),
]