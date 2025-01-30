from django.contrib import admin
from .models import images
@admin.register(images)
class imagesadmin(admin.ModelAdmin):
    list_display=['brand','photo','bvar','bprice','hvar','hprice']
