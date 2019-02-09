from django.db import models
from datetime import datetime
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from comment.models import Comment
# Create your models here.

####################################################
########Post Category Model ,Ex:HTML,CSS,###########
class Category(models.Model):
	name=models.CharField(max_length=150)
	
	def __str__(self):
		return self.name
		


####################################################
########Post  Model ###########

class Post(models.Model):
	title=models.CharField(max_length=255)
	description=models.TextField()
	image=models.ImageField(upload_to='.',default='default.png',null=False,blank=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	pub_date = models.DateTimeField(auto_now_add=True, blank=True)
	update_date = models.DateTimeField(auto_now=True,null=True,blank=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):#this will return the link to detail view according to its pk
		return reverse("postDetail",kwargs={'id':self.id})
	def get_delete_url(self):#this will return the link to Delete view according to its pk
		return reverse("postDelete",kwargs={'id':self.id})
	def get_update_url(self):#this will return the link to Update view according to its pk
		return reverse("postUpdate",kwargs={'id':self.id})
	def comment(self):#this will return all the comments for this post
		return Comment.objects.filter_by_instance(self)	
	def get_content_type(self):#this will return the class id from content type 
		return ContentType.objects.get_for_model(self.__class__)	