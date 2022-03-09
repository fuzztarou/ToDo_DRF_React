from django.contrib import admin

from .models import Item

class ItemAdmin(admin.ModelAdmin):
    fields = ['item', 'pic']

admin.site.register(Item, ItemAdmin)