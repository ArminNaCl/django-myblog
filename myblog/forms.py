from django import forms
from .models import Comment
from django.utils.translation import ugettext_lazy as _

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = {'content',}
        labels = {'content':_('Comment') }
        help_text = {
                    'content' :_("enter your comment about this post"),
        }
        
        widgets={
            'content': forms.Textarea(attrs={'class':"form-control"}),

        }