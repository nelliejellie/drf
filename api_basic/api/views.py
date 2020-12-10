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
# for website authentication
from django.contrib.auth.decorators import login_required
# for class based views web login
from django.utils.decorators import method_decorator



# for posting gettimg list of articles
@login_required
@csrf_exempt
@api_view(['GET','POST'])
def article_list(request):
    if request.method == "GET":
        article = Article.objects.all()
        serializer = ArticleSerializer(article, many=True)
        return Response(serializer.data)

    elif  request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.data, status=status.HTTP_400_BAD_REQUEST)


# for getting a particular article, delete or editing it
@login_required
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

    @method_decorator(login_required)
    def get(self, request):
        articles =  Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    
    @method_decorator(login_required)
    def post(self, request):
        serializer = ArticleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

# class detail list

class ArticleDetail(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    @method_decorator(login_required)
    def get_object(self, id):
        try:
            article = Article.objects.get(id=id)
        except article.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @method_decorator(login_required)
    def get(self, id, request):
        article = self.get_object(id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    @method_decorator(login_required)
    def put(self, request, id):
        article = self.get_object(id)
        serializer = ArticleSerializer(article, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
    @method_decorator(login_required)
    def delete(self, request, id):
        article = self.get_object(id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
