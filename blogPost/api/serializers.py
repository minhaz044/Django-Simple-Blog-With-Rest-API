from rest_framework import serializers
from blogPost.models import Post

class PostListSerializer(serializers.ModelSerializer):
	class Meta:
		model=Post
		fields=[
			'id',
			'title',
			'image',
			'description',
			'category',
			'author',
			'pub_date'
		]


class PostDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model=Post
		fields=[
			'title',
			'image',
			'description',
			'category',
			'author',
			'pub_date'
		]

class PostUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model=Post
		fields=[
			'title',
			'image',
			'description',
			'category',
		]

class PostCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model=Post
		fields=[
			'title',
			'image',
			'description',
			'category',
			'author',
			'pub_date'
		]
