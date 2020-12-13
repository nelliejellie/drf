from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .serializers import ArticleSerializer
from ..models import Article
#for post updates
from django.views.decorators.csrf import csrf_exempt
# to get access to the browsableapi renderer import decorators
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# for class based views
from rest_framework.views import APIView
# for api autherntication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# importing the user model
from django.contrib.auth.models import User
import cloudinary




# for posting getting list of articles
@csrf_exempt
@api_view(['GET','POST'])
def article_list(request):
    if request.method == "GET":
        article = Article.objects.all()
        serializer = ArticleSerializer(article, many=True)
        return Response(serializer.data)

    elif  request.method == 'POST':
        user = User.objects.get(pk=request.user.id)
        article = Article(user=user)
        serializer = ArticleSerializer(article, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.data, status=status.HTTP_400_BAD_REQUEST)


# for getting a particular article, delete or editing it
@csrf_exempt
@api_view(['GET','PUT','DELETE'])
def article_detail(request, pk):
    try:
        article = Article.objects.get(pk=pk)
    except article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class based view for detail and article list

# class article list

class ArticleApiView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    
    def get(self, request):
        articles =  Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    
    
    def post(self, request):
        user = User.objects.get(pk=request.user.id)
        article = Article(user=user)
        serializer = ArticleSerializer(article, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

# class detail list

class ArticleDetail(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, id):
        try:
            article = Article.objects.get(id=id)
        except article.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, id, request):
        article = self.get_object(id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, id):
        article = self.get_object(id)
        serializer = ArticleSerializer(article, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        article = self.get_object(id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# view for the first 10 objects in the api
@csrf_exempt
@api_view(['GET'])
def get_ten_article_list(request):
    if request.method == "GET":
        article = Article.objects.all()[:10]
        serializer = ArticleSerializer(article, many=True)
        return Response(serializer.data)

# get articles that concern endsarz alone
@csrf_exempt
@api_view(['GET'])
def get_endsars(request):
    if request.method == "GET":
        article = Article.objects.filter(categories='EndSars')
        serializer = ArticleSerializer(article, many=True)
        return Response(serializer.data)

# get articles that concern endsarz alone
@csrf_exempt
@api_view(['GET'])
def get_covid19(request):
    if request.method == "GET":
        article = Article.objects.filter(categories='Covid-19')
        serializer = ArticleSerializer(article, many=True)
        return Response(serializer.data)

