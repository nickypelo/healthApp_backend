from django.db import models
from django.contrib.auth.models import User


# Users and their tokens
class Tokens(models.Model):
    pass


# For User ProfilePicture
class ProfilePicture(models.Model):
    image_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.FileField(upload_to='images/Profile')

    def __str__(self):
        return self.image_owner


# For User comparison pictures
class ProgressPhotos(models.Model):
    photo_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    before_photo = models.FileField(upload_to='images', null=True)
    after_photo = models.FileField(upload_to='images', null=True)

    def __str__(self):
        return self.photo_owner
