from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager

# Create your models here.

class Post(models.Model):
    POST_STATUS={('A','ACTIVE'),('D',"INACTIVE"),}
    title = models.CharField(max_length=200)
    image = models.ImageField(default='default.png',blank=True)
    slug = models.SlugField()
    description = models.TextField(blank=True,default='')
    release_date = models.DateTimeField(blank=True)
    language = models.CharField(default='', max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.CharField(default='A', max_length=50,choices=POST_STATUS)
    tags = TaggableManager()
    
    def __str__(self):
        return self.title
    
    def TruncateStringTo50(self):
        return self.description[0:80]+"..."	
        
    def get_absolute_url(self):
        return reverse('blog:blog_detail',kwargs={'pk':self.pk})

    class Meta:
        ordering = ('-created_date',)
		

class Comment(models.Model):
    post_obj = models.ForeignKey(Post, related_name="post_comment", on_delete=models.CASCADE)
    comment_title = models.CharField(max_length=255)
    ratings = models.IntegerField(default=0)
    body = models.TextField(default='')
    created_date = models.DateTimeField( auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    comment_status = models.BooleanField(default=True)
    

    class Meta:
    	ordering=['-updated_date','-ratings']
	
    def __str__(self):
        return 'Comment by {} on {}'.format(self.comment_title, self.post_obj)
