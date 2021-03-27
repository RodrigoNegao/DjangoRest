from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from Foods.models import Food
from django.db.models import Q

def index(request):
  listings = Food.objects.order_by('-list_date').filter(is_published=True)

  paginator = Paginator(listings, 6)
  page = request.GET.get('page')
  paged_listings = paginator.get_page(page)

  context = {
    'listings': paged_listings
  }  

  return render(request, 'listings/listings.html', context)

def listing(request, slug_text):
  #listing = get_object_or_404(Listing, pk=listing_id)
  listing = get_object_or_404(Food, slug=slug_text)

  context = {
    'listing': listing
  }

  return render(request, 'listings/listing.html', context)

def search(request):  
  queryset_list = Food.objects.order_by('-list_date').filter(is_published=True)

  # Keywords
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      #   # | == OR
      # food_filter = (Q(productName__icontains=search_query) 
      #                   | Q(description__icontains=search_query) )
      queryset_list = queryset_list.filter(description__icontains=keywords)

  # City
  if 'city' in request.GET:
    city = request.GET['city']
    if city:
      queryset_list = queryset_list.filter(city__icontains=city) #(Q(city__icontains=city))

  # Price
  if 'price' in request.GET:
    price = request.GET['price']
    if price != "":
      queryset_list = queryset_list.filter(price__lte=price) 
 
  # Rent Price
  if 'rent_price' in request.GET:
    rent_price = request.GET['rent_price']
    if rent_price != "":
      queryset_list = queryset_list.filter(rent_price__lte=rent_price)

  paginator = Paginator(queryset_list, 6)
  page = request.GET.get('page')
  paged_listings = paginator.get_page(page)
  
  context = {
    # 'price_choices': price_choices,
    'listings': paged_listings,
    'values': request.GET
  }

  return render(request, 'listings/search.html', context)

  
def food_update_view(request, slug_text): #pk 

    product_list = Product.objects.all()

    product_choice = Product.objects.filter(slug=slug_text)

    product = get_object_or_404(product_list, slug=slug_text)
     
    if request.method == 'POST':

        product_update_form = ProductForm(data=request.POST,files=request.FILES,instance=product)
        # Check to see the form is valid
        if product_update_form.is_valid(): # and profile_default.is_valid() :
            # Sava o produto
            product_update_form.save()
            # Registration Successful! messages.success
            messages.success(request, 'Produto Modificado com Sucesso')
            #Go to Index
            return HttpResponseRedirect(reverse('index'))
        else:
            # One of the forms was invalid if this else gets called.
            print(product_update_form.errors)

    else:
        # render the forms with data.
        product_update_form = ProductForm(instance=product)

        print(product_update_form)
    
    context = {'product_update_form': product_update_form, 'product_choice':product_choice ,'product_list': product_list}
    return render(request, 'base/update.html',context)

    


def food_delete_view(request,slug_text):
    # dictionary for initial data with  
    # field names as keys
    product_choice = Food.objects.filter(slug=slug_text)

    context ={'product_choice':product_choice} 
  
    # fetch the object related to passed id 
    obj = get_object_or_404(Product, pk = pk)   
  
    if request.method =="POST": 
        # delete object 
        obj.delete() 
        # Registration Successful! messages.success
        messages.success(request, 'Produto Apagado com Sucesso')
        #Go to Index
        return HttpResponseRedirect(reverse('index')) 
  
    return render(request, "base/delete.html", context) 
