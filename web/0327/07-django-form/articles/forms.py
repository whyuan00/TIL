from django import forms 
from .models import Article 

# form태그를 클래스 형태로 쓸것

# 입력받아서 다른 용도로 쓸때 -> 로그인 
#class ArticleForm(forms.Form):
#    title = forms.CharField(max_length=10)
#    content = forms.CharField(widget=forms.Textarea) # 모델필드에서 맥스랭스는 필수인자 

# 받은 정보를 모두 받아서 데이터베이스에 저장할떄 
class ArticleForm(forms.ModelForm):

    #위젯에 csss 입히기 위해서 
    title = forms.CharField(
        label = '제목',
        widget= forms.TextInput(
            #위젯클래스의 어트리뷰트 인자에 넣어야함 
            attrs = {
                'class':'my-title',
                'placeholdr': 'Enter the title',
                # 이렇게하면 class='mytitle'롣 ㅡㄹ어감 
            }

        ),

    )  

    #메타데이터란 데이터의 데이터 
    # 모델폼은 아티클에서 title과 content만 받아서 알아서 위젯만들어줌
    class Meta: 
        model = Article
        fields = '__all__' #('title','content')
        #뺄수도있음: exclude 
        # exclude =('title',)