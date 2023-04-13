from django.db import models
from django.utils import timezone

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    end_date = models.DateTimeField()

    def deadline(self):
        end_date = self.end_date
        today = timezone.now()
        d_day = (end_date - today).days
        return d_day

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['end_date']


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


class Comment(models.Model):
   article = models.ForeignKey(Article, on_delete=models.CASCADE)
   content = models.CharField(max_length=200)
   updated_date = models.DateTimeField(auto_now=True)
   parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True)

   def __str__(self):
       return self.content


