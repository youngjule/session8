from django.db import models
from django.utils import timezone

# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name





class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    time = models.DateTimeField(auto_now = True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)  # 'category' 필드 추가
    created_date = models.DateTimeField(default=timezone.now) # 작성 시간

    def __str__(self):
        return self.title


