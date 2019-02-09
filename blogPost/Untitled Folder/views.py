from django.shortcuts import render,get_object_or_404
from django.views import View
from .models import Post,Category
from blogPost.form import PostCreateForm

# Create your views here.

class Base(object):
	context={}
	categories=Category.objects.all()
	context['categories']=categories
	#other common data goes here 	


class PostListView(View,Base):
	
	template_name='home.html'
	queryset=Post.objects.all()

	def get(self,request,*args,**kwargs):
		self.context['object_list']=self.queryset
		return render(request,self.template_name,self.context)


class PostDetailView(View,Base):
	
	template_name='postDetail.html'

	def get(self,request,id=None,*args,**kwargs):
		if id is not None:
			post=Post.objects.get(pk=id)
			self.context['post']=post	
		return render(request,self.template_name,self.context)


class PostCreateView(View,Base):
	
	template_name='postCreate.html'

	def get(self,request,*args,**kwargs):
		
		createform=PostCreateForm
		self.context['form']=createform()
		return render(request,self.template_name,self.context)
	