from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# Create your views here.
def index_view(request):
    token = Token.objects.get(user=request.user).key
    context = {
        'token': token,
    }
    return render(request, 'pages/index.html', context)