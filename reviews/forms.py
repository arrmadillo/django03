from django import forms
from .models import Review, Comment

class ReviewForm(forms.ModelForm):
    rating = forms.FloatField(widget=forms.NumberInput(attrs={'step': 0.5}))

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

    