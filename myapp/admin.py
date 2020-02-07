from django.contrib import admin
from.models import REG
# Register your models here.
class Regadmin(admin.ModelAdmin):
    list_display = ["usermob","Fname","Lname","pwd"]
    list_filter = ['usermob']
admin.site.register(REG,Regadmin)