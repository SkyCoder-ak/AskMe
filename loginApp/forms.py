from django import forms

class LoginForm(forms.Form):
    # email = forms.EmailField(label='Email', max_length=150)
    username = forms.CharField(label='Username', max_length=50)
    password = forms.CharField(label='Password', max_length=16, widget=forms.PasswordInput)