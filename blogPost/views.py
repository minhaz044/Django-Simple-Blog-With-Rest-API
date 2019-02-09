#################Import Section#############################
from django.shortcuts import render,get_object_or_404,redirect
from django.http import Http404  
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType

from django.views import View
from .models import Post,Category
from blogPost.form import PostCreateForm
from comment.form import CommentForm,CommentReplyForm
from django.core.paginator import Paginator
from comment.models import Comment
###########################################################






##################This is our base class#############
"""menu list and ,number of post  in menu and 
			other common attribute  are fitched
				in this section """
##########################################################
class Base(object):
	context={}
	categories=Category.objects.all()
	context['categories']=categories
###########################################################


#class CommonOperation():





##################This is POst Create view #############
########to upload file request.File must be sent########
class PostCreateView(View,Base):	
	template_name='postCreate.html'
	def get(self,request,*args,**kwargs):
		form=PostCreateForm()
		self.context['form']=form
		return render(request,self.template_name,self.context)

	def post(self,request,*args,**kwargs):
		form=PostCreateForm(request.POST,request.FILES)
		if form.is_valid():
			if request.user.is_authenticated:
				mypost=form.save(commit=False)
				mypost.author=request.user
				mypost.save()
				messages.success(request, 'Post Created Successfully.')
				return redirect('postDetail',id=mypost.pk)
			else:
				messages.warning(request, 'User is not authenticated')	
		self.context['form']=form
		return render(request,self.template_name,self.context)

###################################################################






##################This is POst Delete view #############
########when form is submited in post method we will delete our object ########
########before delete we need to check author #######
class PostDeleteView(View,Base):	
	template_name='postDelete.html'
	def get_delete_post(self):
		id=self.kwargs.get('id')
		if id is not None:
			post=get_object_or_404(Post,pk=id)
			return post
		else:
			return None

	def get(self,request,id=None,*args,**kwargs):
		post=self.get_delete_post()
		if post is not None and post.author == request.user:
			self.context['post']=post
			return render(request,self.template_name,self.context)
		else:
			raise Http404

	def post(self,request,id=None,*args,**kwargs):
		post=self.get_delete_post()
		if post is not None and post.author == request.user:
			post.delete()
			self.context['post']=None
			messages.success(request,'Post Deleted Successfully.')
			return redirect('home')
		else:
			raise Http404

###################################################################









##################This is single post detail view #############
############there is too many Copy code ,need to Optimize it ##########
#################Generic Class View Will reduce Code Length###########
class PostDetailView(View,Base):
	template_name='postDetail.html'
	def get(self,request,id=None,*args,**kwargs):
		if id is not None:
			post_instance=get_object_or_404(Post,pk=id)
			initial_data={
			"content_type":post_instance.get_content_type(),
			"object_id":post_instance.id
			}
			comment_form=CommentForm(None,initial=initial_data)
			self.context['post']=post_instance
			self.context['comment_form']=comment_form
		return render(request,self.template_name,self.context)
	def post(self,request,id=None,*args,**kwargs):
		if id is not None:
			post_instance=get_object_or_404(Post,pk=id)
			initial_data={
			'content_type':post_instance.get_content_type(),
			'object_id':post_instance.id
			}
			comment_form=CommentForm(request.POST)
			if request.user.is_authenticated:
				if comment_form.is_valid():
					my_comment=comment_form.save(commit=False)
					my_comment.user=request.user
					my_comment.save()	
					messages.success(request, 'Comment Created Successfully.')
					return redirect('postDetail',id=post_instance.pk)
		return render(request,self.template_name,self.context)

#######################################################










##################This is index or home view #############
class PostListView(View,Base):
	
	template_name='home.html'

	def get(self,request,*args,**kwargs):
		queryset=Post.objects.all().order_by('-pub_date')
		paginator=Paginator(queryset,10)
		page_name='page'
		page_number=request.GET.get(page_name)
		object_list=paginator.get_page(page_number)	
		self.context['object_list']=object_list
		self.context['page_name']=page_name
		return render(request,self.template_name,self.context)
##########################################################







##################This is POst Update view #############
########to upload file request.File must be sent########
class PostUpdateView(View,Base):	
	template_name='postUpdate.html'
	def get_delete_post(self):
		id=self.kwargs.get('id')
		if id is not None:
			post=get_object_or_404(Post,pk=id)
			return post
		else:
			return None
	def get(self,request,id=None,*args,**kwargs):
		instance=self.get_delete_post()
		form=PostCreateForm(instance=instance)
		self.context['form']=form
		return render(request,self.template_name,self.context)

	def post(self,request,*args,**kwargs):
		instance=self.get_delete_post()
		form=PostCreateForm(request.POST,request.FILES,instance=instance)
		if form.is_valid():
			mypost=form.save(commit=False)
			mypost.author=request.user
			mypost.save()
			messages.success(request, 'Post updated.Successfully')
			return redirect('postDetail',id=mypost.pk)
		else:
			messages.warning(request, 'Failed to  updated.')
			self.context['form']=form
			return render(request,self.template_name,self.context)

###################################################################


