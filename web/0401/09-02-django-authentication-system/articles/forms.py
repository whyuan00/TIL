from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

#Manager isn't available; 'auth.User' has been swapped for 'accounts.User'
    