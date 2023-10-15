from django.contrib import admin
from .models import ProfilePicture, ProgressPhotos


# register ProfilePicture model
admin.site.register(ProfilePicture)

# register ProgressPhoto model
admin.site.register(ProgressPhotos)

