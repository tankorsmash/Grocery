from django.contrib.admin import site

from grocery.models import Company, Store, Aisle, FoodItem

site.register(Company)
site.register(Store)
site.register(Aisle)
site.register(FoodItem)
