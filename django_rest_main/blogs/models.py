from django.db import models

class Blog(models.Model):
    Blog_title = models.CharField(max_length=50)
    Blog_body = models.TextField()
    
    def __str__(self):
        return self.Blog_title
    

class Comment(models.Model):
    blog = models.ForeignKey(Blog , on_delete= models.CASCADE , related_name='comments')
    comment = models.TextField()
    def __str__(self):
        return self.comment
    