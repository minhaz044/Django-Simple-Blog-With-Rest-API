from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.conf import settings

# Create your models here.
class CommentManager(models.Manager):
	def filter_by_instance(self,instance=None,*args,**kwargs):
		if instance is not None:
			object_type=ContentType.objects.get_for_model(instance.__class__)
			return super(CommentManager,self).filter(content_type=object_type,object_id=instance.id)
		




class Comment(models.Model):
	user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')
	content=models.TextField()
	timestamp=models.DateTimeField(auto_now_add=True)
	"""docstring for Comment"""
	objects=CommentManager()
	def __str__(self):
		return str(self.content)

	def sub_comment(self):
		object_type=ContentType.objects.get_for_model(self.__class__)
		return Comment.objects.filter(content_type=object_type,object_id=self.id)
		