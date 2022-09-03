from django.contrib import admin
from .models import Catagory,Post,Contact

# Register your models here.

# for configuring the admin catagory interface
class CatagoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title','description','url','add_date')
    search_fields = ('title',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('cat',)
    list_per_page: 50

    class Media:
        js = ('https://cdn.tiny.cloud/1/no-api-key/tinymce/6/tinymce.min.js', 'JS/script.js',)

admin.site.register(Catagory , CatagoryAdmin)
admin.site.register(Post , PostAdmin)
admin.site.register(Contact)