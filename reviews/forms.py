from django import forms
from .models import Review, Comment

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ["user"]
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'content': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
            'movie': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }

class CommentForm(forms.ModelForm):
    # content = forms.CharField(
    #     widget=forms.TextInput()
    # )
   
    
    class Meta:
        model = Comment
        fields = ('content',)

    