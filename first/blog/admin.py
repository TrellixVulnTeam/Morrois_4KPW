from django.contrib import admin

# Register your models here.
from .models import Product
from import_export.admin import ImportExportModelAdmin




@admin.register(Product)
class ViewAdmin(ImportExportModelAdmin):
    pass
