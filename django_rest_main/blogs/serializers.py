from rest_framework import serializers
from  .models import Blog , Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
 

class BlogSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many = True , read_only = True ) # This will bring all the comment of a paticular blog . 
    # Note: you have to make the name same as related name of blog model 
    # This single line of code will make you serializer a nested serializer
    class Meta:
        model = Blog
        fields = '__all__'