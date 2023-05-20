from django import forms 
from accounts.models import User 
from django.contrib.auth.forms import UserCreationForm,UsernameField,AuthenticationForm


class RegisterForm(UserCreationForm):
    
    password1 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'Şifre',
                'class' : 'login-input',
            }))

    password2 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'Şifreni tekrarla',
                'class' : 'login-input',
            }))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','password1','password2')

        widgets = {
            'username': forms.TextInput(attrs={'id': 'username', 'placeholder': 'Kullanıcı adı', 'class': 'login-input'}),
            'first_name': forms.TextInput(attrs={'id': 'full_name', 'placeholder': 'Adı Soyadı', 'class': 'login-input'}),
            'last_name': forms.TextInput(attrs={'id': 'last_name', 'placeholder': 'Cep Telefonu Numarası veya E-posta', 'class': 'login-input'}),
        }


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={
        'autofocus': True,
        'class': 'inputs',
        'placeholder': 'Username',
        'name': 'username'
    }))
    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'current-password',
            'class': 'inputs',
            'name': 'password',
            'placeholder': 'Password'
        }),
    )

    class Meta:
        model = User
        fields = ['username', 'password']

# class UpdateForm(EmailResetForm):
#     username = UsernameField(widget=forms.TextInput(attrs={
#         'autofocus': True,
#         'class': 'inputs',
#         'placeholder': 'Username',
#         'name': 'username'
#     }))
#     model = User
#     fields = {'username'}
