from django.urls import path
from . import views

urlpatterns = [
    path('article/', views.article_list),
    path('detail/<int:pk>', views.article_detail),
    # the class based views paths
    path('classArticle/', views.ArticleApiView.as_view()),
    path('classDetail/<int:pk>', views.ArticleDetail.as_view()),
    # get 10 articles
    path('tenArticles/', views.get_ten_article_list),
    # articles that are related to endsars
    path('endsars/', views.get_ten_article_list),
    # articles that are related to endsars
    path('endsars/', views.get_endsars),
    # articles that are related to endsars
    path('covid19/', views.get_covid19),
]