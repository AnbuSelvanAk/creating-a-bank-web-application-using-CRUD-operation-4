from django.contrib import admin
from apps.models import Bank
class BankAdmin (admin.ModelAdmin):
	list_display=['acno','name','depamnt','bal']

admin.site.register(Bank,BankAdmin)