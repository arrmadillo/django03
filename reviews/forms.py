from django import forms
from .models import Review, Comment

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ["user"]

class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'style': 'width:94%',
                'id': 'commentinput',
            },
        ),
    )
   
    
    class Meta:
        model = Comment
        fields = ('content',)

    