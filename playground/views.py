from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
from store.models import Product, Collection, Orderitem
from tags.models import TaggedItem

# Create your views here.


def hello(request):
    # Example: fetch products with price less than 100
    # queryset = Product.objects.filter(price__gt=1900)
    # queryset = Product.objects.filter(
    #     # price between 1500 and 1550
    #     price__range=(1500, 1550)).order_by('price')
    # queryset = Product.objects.filter(name__icontains='coffee')
    # queryset = Product.objects.filter(updated_at__year=2024)
    # queryset = Product.objects.filter(inventory__lt=10, price__lt=2000)
    # queryset = Product.objects.filter(
    # inventory__lt=10).filter(price__lt=2000)
    # queryset = Product.objects.filter(
    #     # Q objects for complex queries with OR logic
    #     Q(inventory__lt=10) | Q(price__lt=2000))
    # queryset = Product.objects.filter(
    #     # Q objects for complex queries with AND     logic
    #     Q(inventory__lt=10) & Q(price__lt=2000))
    # queryset = Product.objects.filter(inventory=F("price"))
    # print(queryset.query)
    # queryset = Product.objects.values(
    #     "id", "name", "price", "collection__name")
    # queryset = Orderitem.objects.values("product_id").distinct()
    # queryset = Product.objects.filter(
    #     id__in=Orderitem.objects.values("product_id").distinct()).order_by('name')
    queryset = TaggedItem.objects.get_tags_for(Product, 11)
    # print(queryset)
    return render(request, "hello.html", {"name": "Sabir Zafar", "products": list(queryset)})
    # return HttpResponse("Hello World!")
