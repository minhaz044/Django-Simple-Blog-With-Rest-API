from django import forms
from comment.models import Comment

class CommentForm(forms.ModelForm):
	class Meta:
		model=Comment
		fields=['content_type','object_id','content'
		]
		widgets={
			'content_type':forms.HiddenInput(),
			'object_id':forms.HiddenInput(),
			'content':forms.Textarea(attrs={'rows':2})
		}


class CommentReplyForm(forms.ModelForm):
	class Meta:
		model=Comment
		fields=['content_type','content'
		]
		widgets={
			'content_type':forms.HiddenInput(),
			'content':forms.Textarea(attrs={'rows':2})
		}








