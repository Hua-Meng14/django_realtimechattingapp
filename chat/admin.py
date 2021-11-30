from django.contrib import admin
from.models import Room, Message
# Register your models here.
#adminsuperuser credentials:
# username:admin
# password: djangochatapp123

admin.site.register(Room)
admin.site.register(Message)