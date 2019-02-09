from django import forms
from blogPost.models import Post,Category


class PostCreateForm(forms.ModelForm):
	class Meta:
		model=Category
		fields=['name'

		]
"""
	
	title=forms.CharField()
	description=forms.CharField()
	img=forms.ImageField(upload_to='blog/static/images/', null=True,blank=True)
	category = forms.ForeignKey(Category, on_delete=models.CASCADE)
	author=forms.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	pub_date = forms.DateTimeField(auto_now_add=True, blank=True)
	update_date = forms.DateTimeField(null=True,blank=True)
"""