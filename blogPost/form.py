from django import forms
from blogPost.models import Post,Category


class PostCreateForm(forms.ModelForm):
	class Meta:
		model=Post
		exclude=['author']







		