from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Messages,Comments,Status
# Register your models here.
admin.site.register(Messages)
admin.site.register(Comments)
admin.site.register(Status)