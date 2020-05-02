from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Madde Açan Kişi")
    title = models.CharField(max_length = 50,verbose_name = "Başlık")
    firma = models.CharField(max_length = 50, verbose_name= "Sorumlu Firma")
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    article_image = models.FileField(blank = True,null = True,verbose_name="Fotoğraf Ekle")
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']

class CloseArticle(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="closeArticle", verbose_name="Kapanma Maddesi")
    close_author = models.ForeignKey("auth.User",on_delete=models.CASCADE, verbose_name = "Maddeyi Kapatan Kişi")
    close_content = models.CharField(max_length = 200,verbose_name = "Yorum")
    close_image = models.FileField(blank = True,null = True,verbose_name="Fotoğraf Ekle")
    close_date = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete = models.CASCADE,verbose_name = "Makale",related_name="comments")
    comment_author = models.CharField(max_length = 50,verbose_name = "İsim")
    comment_content = models.CharField(max_length = 200,verbose_name = "Yorum")
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content
    class Meta:
        ordering = ['-comment_date']