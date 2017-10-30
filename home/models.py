from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(verbose_name='Заголовок',max_length=30)
    text = models.TextField(verbose_name='Тест',max_length=300)
    image = models.ImageField(blank=True,null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title