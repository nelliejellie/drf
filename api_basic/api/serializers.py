from rest_framework import serializers
from ..models import Article


class ArticleSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = Article
        fields = ['id','username','categories','author','quote', 'date','image']

    def get_username(self, Article):
        username = Article.user.username
        return username