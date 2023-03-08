from django import forms
from django.contrib.auth.models import User
from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['class']= 'form-control col-6'
        self.fields['last_name'].widget.attrs['class']= 'form-control col-6'
        self.fields['email'].widget.attrs['class']= 'form-control'

        
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('apelido', 'date_of_birth', 'resumo')

    def __init__(self, *args, **kwargs):
        super(ProfileEditForm, self).__init__(*args, **kwargs)
        self.fields['apelido'].widget.attrs['class']= 'form-control'
        self.fields['date_of_birth'].widget.attrs['class']= 'form-control'
        self.fields['resumo'].widget.attrs['class']= 'form-control'


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('photo', )