import json
from django.contrib.auth.models import User
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


# Registration
# @api_view(['GET'])
def register(request):
    if request.method == 'POST':
        form_data = json.loads(request.body)
        # extract the necessary registration details
        username = form_data['userName']
        firstname = form_data['firstName']
        lastname = form_data['lastName']
        email = form_data['email']
        password = form_data['password']

        user = User.objects.create_user(username, email, password, first_name=firstname, last_name=lastname)
        user.save()

        return JsonResponse({'message': 'successfully registered'})
    else:
        return JsonResponse({'Error': 'Try again.'})
