from django import forms

class UserRegForm(forms.Form):
    full_name = forms.CharField(label='Full Name', max_length=60)
    dis_name = forms.CharField(label='Display Name', max_length=30)
    email = forms.EmailField(label='Email', max_length=150)
    password = forms.CharField(label='Password', max_length=16, widget=forms.PasswordInput)