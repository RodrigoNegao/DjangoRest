from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q

from .forms import FoodForm
from Foods.models import Food

def index(request):
  listings = Food.objects.order_by('-list_date').filter(is_published=True)

  paginator = Paginator(listings, 6)
  page = request.GET.get('page')
  paged_listings = paginator.get_page(page)

  context = {
    'listings': paged_listings
  }  

  return render(request, 'base/index.html', context)

def listing(request, slug_text):
  #listing = get_object_or_404(Listing, pk=listing_id)
  listing = get_object_or_404(Food, slug=slug_text)

  context = {
    'listing': listing
  }

  return render(request, 'base/listing.html', context)

def search(request):  
  queryset_list = Food.objects.order_by('-list_date').filter(is_published=True)

  # Keywords
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      #   # | == OR
      # queryset_list = (Q(foodName__icontains=keywords) 
      #                   | Q(description__icontains=keywords) | Q(price__icontains=keywords)  )
      queryset_list = queryset_list.filter(description__icontains=keywords)

  # Price
  if 'price' in request.GET:
    price = request.GET['price']
    if price != "":
      queryset_list = queryset_list.filter(price__lte=price) 

  paginator = Paginator(queryset_list, 6)
  page = request.GET.get('page')
  paged_listings = paginator.get_page(page)
  
  context = {
    # 'price_choices': price_choices,
    'listings': paged_listings,
    'values': request.GET
  }

  return render(request, 'base/search.html', context)

  
def food_update_view(request, slug_text): #pk 

    food_list = Food.objects.all()

    food_choice = Food.objects.filter(slug=slug_text)

    food = get_object_or_404(food_list, slug=slug_text)
     
    if request.method == 'POST':

        food_update_form = FoodForm(data=request.POST,files=request.FILES,instance=food)
        if food_update_form.is_valid():
            food_update_form.save()
            messages.success(request, 'Produto Modificado com Sucesso')
            #Go to Index
            return HttpResponseRedirect(reverse('index'))
        else:
            print(food_update_form.errors)

    else:
        food_update_form = FoodForm(instance=food)

        print(food_update_form)
    
    context = {'food_update_form': food_update_form, 'food_choice':food_choice ,'food_list': food_list}
    return render(request, 'base/update.html',context)

    


def food_delete_view(request,slug_text):
    # dictionary for initial data with  
    # field names as keys
    food_choice = Food.objects.filter(slug=slug_text)

    context ={'food_choice':food_choice} 
  
    # fetch the object related to passed id 
    obj = get_object_or_404(Food, slug=slug_text)   
  
    if request.method =="POST": 
        # delete object 
        obj.delete() 
        # Registration Successful! messages.success
        messages.success(request, 'Produto Apagado com Sucesso')
        #Go to Index
        return HttpResponseRedirect(reverse('index')) 
  
    return render(request, "base/delete.html", context) 
