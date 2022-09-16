from django.contrib import admin

import productos
from productos.models import Producto

# Register your models here.
admin.site.register(Producto)