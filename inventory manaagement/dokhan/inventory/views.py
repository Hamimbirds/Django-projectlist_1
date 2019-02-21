from django.shortcuts import render
from.models import Item

# Create your views here.
def item_list(request):
    all_items = Item.objects.all()
    context = {'all_items':all_items}
    return render(request, 'inventory/item_list.html', context)