import uuid
import os
from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField 
from django.utils.html import strip_tags


class Blog(models.Model):
    title = models.CharField(max_length=100)

    thumb_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    content = HTMLField() # models.TextField()에서 수정   
    
    author = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, help_text="블로그 글의 카테고리를 선택하세요.")
    view_count = models.PositiveIntegerField(default=0)
    tags = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'


class Comment(models.Model):
    post = models.ForeignKey(
        Blog, on_delete=models.CASCADE, related_name='comments'
    )
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    # 댓글 삭제시 DB에서 완전히 지우지 않고, 안 보이도록 설정하기 위함.
    is_deleted = models.BooleanField(default=False)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self):
        if self.is_deleted:
            return "삭제되었습니다."
        else:
            # HTML 등을 제거
            return strip_tags(self.message)
    
    
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name
    

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, help_text="블로그 글을 분류를 입력하세요. ex)소설")

    def __str__(self):
        return self.name
    
