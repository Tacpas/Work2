from django.contrib import admin
from tacpasapp.models import Contact

# Register your models here.
class Contactadmin(admin.ModelAdmin):
    list_display=['name','email','message']

admin.site.register(Contact,Contactadmin)