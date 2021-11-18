from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    program = (
        ('python', 'python'),
        ('php', 'php'),
        ('java_script', 'java_script'),
        ('html_css', 'html_css'),
        ('django', 'django'),
        ('ネットセキュリティー', 'ネットセキュリティー'),
        ('server', 'server'),
        ('error', 'error'),
    )
    categoly = models.CharField("カテゴリー", max_length=50, null=True, choices=program)
    title = models.CharField("タイトル", max_length=50, null=False)
    content = models.TextField("本文", null=False)
    date_posted = models.DateTimeField("作成日", default=timezone.now)
    
    def __str__(self):
        return self.title + ' | ' + str(self.content)
