from rest_framework import serializers
from .models import Article


#DRF 가 장고 에 맞게 문법 유사하게 설계 

class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id','title','content',)
    

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


