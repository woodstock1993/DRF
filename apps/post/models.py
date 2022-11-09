from django.db import models


class Comment(models.Model):
    id = models.CharField(
        primary_key=True,
        unique=True,
        max_length = 128,
        verbose_name="아이디",
    )
    body = models.CharField(
        max_length=512,
        verbose_name="댓글"
    )


class Post(models.Model):
    id = models.CharField(
        primary_key=True,
        unique=True,
        max_length = 128,
        verbose_name="아이디",
    )
    title = models.CharField(max_length=128, verbose_name="블로그 제목")

    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        related_name="post"
        )