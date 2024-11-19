from django.shortcuts import render
from .models import User

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer

# Create your views here.

# def createUser(request):
#     if request.method == "POST":
#         name = request.POST.get('name', '')
#         description = request.POST.get('description', '')
#         status = True
        
#         # Initialize errors dictionary
#         errors = {}

#         # Validate fields
#         if not name:
#             errors['name'] = "Name is required."
#         if not description:
#             errors['description'] = "Description is required."

#         # Save member if no errors
#         if not errors:
#             User.objects.create(name=name, description=description, status=status)
#             return render(request, 'create-user.html')

#         # Re-render the form with errors
#         return render(request, 'create-user.html', {'errors': errors, 'data': request.POST})
#     return render(request, 'create-user.html')  

@api_view(['GET', 'POST'])
def users(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    