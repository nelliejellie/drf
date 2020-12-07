from django.urls import path
from . import views

urlpatterns = [
    path('article/', views.article_list),
    path('detail/<int:pk>', views.article_detail),
    # the class based views paths
    path('classArticle/', views.ArticleApiView.as_view()),
    path('classDetail/<int:pk>', views.ArticleDetail.as_view()),
]