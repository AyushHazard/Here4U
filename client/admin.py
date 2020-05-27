from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Clientdata)
admin.site.register(Counsellordata)

admin.site.register(Description)


admin.site.register(ActiveBookings)
admin.site.register(Bookings)

admin.site.register(Post)
admin.site.register(Message)
admin.site.register(ActiveMessages)
admin.site.register(VideoCallLink)
admin.site.register(sessionNotes)