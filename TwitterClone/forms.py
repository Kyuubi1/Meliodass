from django import forms
from .models import Account, Post, Comment, Like



class QuickLogin(forms.ModelForm):
    class Meta:
        model = Account
        fields = {'username', 'password', }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'username', 'placeholder': 'Tên đăng nhập...'}),
            'password': forms.TextInput(attrs={'class': 'password', 'placeholder': 'Mật khẩu...', 'type': 'password'})
        }


class Signup(forms.ModelForm):
    class Meta:
        model = Account

        fields = {'username', 'password', 'sex', 'email', 'phone', }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'username', 'placeholder': 'Tên đăng nhập...'}),
            'password': forms.TextInput(attrs={'class': 'password', 'placeholder': 'Mật khẩu...', 'type': 'password'}),
            'email': forms.TextInput(attrs={'class': 'email', 'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'phone', 'placeholder': 'Số điện thoại...'}),
            'sex': forms.Select(attrs={'class': 'sex'})
        }


class CreatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = {'user', 'context', }
        widgets ={

            'context': forms.TextInput(attrs={'class': 'contexted', 'placeholder': 'Chuyện gì đang xảy ra ?'})

        }