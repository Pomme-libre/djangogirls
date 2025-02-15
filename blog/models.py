from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    """
    インスタンス作成
    author: 変数名
    models: モジュール名
    ForeignKey: クラス名
    settings.AUTH_USER_MODEL, models.CASCADE: 引数名
    """
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published = timezone.now()
        self.save()

    def __str__(self):
        return self.title
