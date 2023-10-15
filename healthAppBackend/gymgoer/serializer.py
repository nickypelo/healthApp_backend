from rest_framework.serializers import ModelSerializer
from .models import ProfilePicture, ProgressPhotos


# Profile Picture serializer
class ProfilePictureSerializer(ModelSerializer):
    class Meta:
        model = ProfilePicture
        fields = '__all__'


# Progress Photos serializer
class ProgressPhotoSerializer(ModelSerializer):
    class Meta:
        model = ProgressPhotos
        fields = '__all__'
