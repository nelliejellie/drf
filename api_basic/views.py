from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Api_Urls, Article
import random

# Create your views here.
def index_view(request):
    urls = Api_Urls.objects.all()
    random_article = Article.objects.last()
    if request.user.is_authenticated:
        token = Token.objects.get(user=request.user).key
        context = {
            'token': token,
            'url': urls,
            'random_article': random_article,
        }
        return render(request, 'pages/index.html', context)
    return render(request, 'pages/index.html', {'url': urls,'random_article': random_article,})
   