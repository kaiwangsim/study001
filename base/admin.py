from django.contrib import admin

# Register your models here.

from .models import roomclass
from .models import device

admin.site.register(roomclass)
admin.site.register(device)

