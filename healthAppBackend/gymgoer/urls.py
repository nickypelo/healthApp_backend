from django.urls import path
from .views import DisplayList, DisplayOne, ProgressList, ProgressOne

urlpatterns = [
    path('display/', DisplayList.as_view(), name='profiles'),
    path('display/<int:image_owner>/', DisplayOne.as_view(), name='profile'),
    path('progress/', ProgressList.as_view(), name='progress'),
    path('progress/<int:pk>/', ProgressOne.as_view(), name='my_progress')
]
