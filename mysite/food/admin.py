from django.contrib import admin

from .models import Item


admin.site.site_header = "Arun Restaurant"
admin.site.site_title = "Arun Restaurant"
admin.site.index_title = "Arun Food App"

class ItemAdmin(admin.ModelAdmin):
    def change_username_to_default(self,request,queryset):
        queryset.update(item_price=1000)

    change_username_to_default.short_description = 'default_user'
    list_display = ['user_name','item_name','item_desc','item_price','item_image']
    search_fields = ('item_name','item_desc')
    
    


admin.site.register(Item,ItemAdmin)