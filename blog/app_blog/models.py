from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Blog(models.Model):
    author_name=models.ForeignKey(User, related_name="post_author",on_delete=models.CASCADE)
    blog_title=models.CharField(max_length=250,verbose_name="Title")
    slug=models.SlugField(max_length=100,blank=True)
    blog_content=models.TextField(verbose_name="whats on your mind?")
    blog_img=models.ImageField(upload_to="blog_img")
    published_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-published_date']

    def __str__(self):
        return self.blog_title

class Comment(models.Model):
    blog=models.ForeignKey(Blog, related_name="blog_comment", on_delete=models.CASCADE)
    user=models.ForeignKey(User, related_name="user_comment", on_delete=models.CASCADE)
    comment=models.TextField()
    comment_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

class Like(models.Model):
    blog=models.ForeignKey(Blog, related_name="liked_blog",on_delete=models.CASCADE)
    user=models.ForeignKey(User, related_name="like_user", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.blog)+str(self.user)