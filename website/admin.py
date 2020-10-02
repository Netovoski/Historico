from django.contrib import admin
from website.models import *
from import_export.admin import ImportExportModelAdmin
from .models import *
# Register your models here.

# admin.site.register(item)
@admin.register(Hist_voo2015, Hist_voo2016, Hist_voo2017)
class ViewAdmin(ImportExportModelAdmin):
    exclude = ('id', )
