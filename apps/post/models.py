from django.db import models
from apps.member.models import Member


class Post(models.Model):
    id = models.AutoField(
        primary_key=True,
        unique=True,
        verbose_name="아이디",
    )
    title = models.CharField(max_length=128, verbose_name="블로그 제목")
    author = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='author')    
    created = models.DateTimeField(auto_now_add=True, verbose_name="생성 일시")
    updated = models.DateTimeField(auto_now=True, verbose_name="업데이트 일시")



class Comment(models.Model):
    id = models.AutoField(
        primary_key=True,
        unique=True,
        verbose_name="아이디",
    )
    author = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='comment')
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="post", null=True
        )

    body = models.CharField(
        max_length=512,
        verbose_name="댓글"
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name="생성 일시")
    updated = models.DateTimeField(auto_now=True, verbose_name="업데이트 일시")
