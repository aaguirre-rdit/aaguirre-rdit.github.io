from django.db import models
from django.utils import timezone

class Category(models.Model):
    title = models.CharField(max_length=255)
    color = models.CharField(max_length=20,verbose_name='Color',null=True)
    def __str__(self):
        return self.title

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, blank=True,on_delete=models.DO_NOTHING, null=True, default='blue')
    image = models.ImageField(blank=True, null=True,upload_to='gallery')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
