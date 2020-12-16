from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Api_Urls, Article
import random

# Create your views here.
def index_view(request):
    urls = Api_Urls.objects.all()
    article = Article.objects.all()
    #get 3 rand items from the database
    random_article = random.sample(list(article),2)
    if request.user.is_authenticated:
        token = Token.objects.get(user=request.user).key
        context = {
            'token': token,
            'url': urls,
            'random_article': random_article,
        }
        return render(request, 'pages/index.html', context)
    return render(request, 'pages/index.html', {'url': urls,'random_article': random_article,})
   