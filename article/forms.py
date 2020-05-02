from django import forms
from .models import Article, CloseArticle
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title","firma","content","article_image"]

class CloseForm(forms.ModelForm):
    class Meta:
        model = CloseArticle
        fields = ["close_content","close_image"]