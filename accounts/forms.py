from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordChangeForm, UsernameField
from django.contrib.auth import get_user_model
from django import forms

class CustomUserCreationForm(UserCreationForm):
    username = UsernameField(
        label='아이디',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )

    image = forms.ImageField(
        label='프로필 이미지',
        required=False,
        widget=forms.FileInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )

    email = forms.EmailField(
        label='이메일',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )
    
    first_name = forms.CharField(
        label='이름',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )

    last_name = forms.CharField(
        label='성',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )

    password1 = forms.CharField(
        label='비밀번호',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )

    password2 = forms.CharField(
        label='비밀번호확인',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'image', 'password1', 'password2',)


class CustomUserChangeForm(UserChangeForm):
    password = None

    image = forms.ImageField(
        label='프로필 이미지',
        required=False,
        widget=forms.FileInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )

    email = forms.EmailField(
        label='이메일',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )
    
    first_name = forms.CharField(
        label='이름',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )

    last_name = forms.CharField(
        label='성',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )

    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = (
            'image',
            'email',
            'first_name',
            'last_name',
        )


class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        label='아이디',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )

    password = forms.CharField(
        label='비밀번호',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )


class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label='기존 비밀번호',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )

    new_password1 = forms.CharField(
        label='새 비밀번호',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        ),
        help_text='8자 이상 영문 대 소문자 숫자, 특수문자를 사용하세요.',
    )

    new_password2 = forms.CharField(
        label='새 비밀번호 확인',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )

    # class Meta(PasswordChangeForm.Meta):
    #     model = get_user_model()
    #     fields = '__all__'