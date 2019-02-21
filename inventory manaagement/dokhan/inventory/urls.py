from django.urls import path
from .views import item_list

app_name="inventory"


urlpatterns = [
    path('items/', item_list, name='item-list'),
]