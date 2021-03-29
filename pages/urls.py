from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('cadastrar-pratos/', views.add_food, name='add-food'), #<int:listing_id> <slug:slug_text> name='listing'
    path('<slug:slug_text>/update/', views.food_update_view, name='food-update'),
    path('<slug:slug_text>/delete/', views.food_delete_view, name='food-delete'),
    path('pesquisa', views.search, name='search'),
]