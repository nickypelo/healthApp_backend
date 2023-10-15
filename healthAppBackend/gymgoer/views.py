from rest_framework import generics

from .serializer import ProfilePictureSerializer, ProgressPhotoSerializer
from .models import ProfilePicture, ProgressPhotos


# view All Users' Profile Pictures
class DisplayList(generics.ListCreateAPIView):
    queryset = ProfilePicture.objects.all()
    serializer_class = ProfilePictureSerializer


# view Single Users' Profile Pictures
class DisplayOne(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProfilePicture.objects.all()
    serializer_class = ProfilePictureSerializer


# view All Users' Profile Pictures
class ProgressList(generics.ListCreateAPIView):
    queryset = ProgressPhotos.objects.all()
    serializer_class = ProgressPhotoSerializer


# view Single Users' Profile Pictures
class ProgressOne(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProgressPhotos.objects.all()
    serializer_class = ProgressPhotoSerializer
