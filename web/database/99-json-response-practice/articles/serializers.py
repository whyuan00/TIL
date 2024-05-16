from rest_framework import serializers
from .models import Article


#모델폼이랑 비슷하게 생김 
class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'
