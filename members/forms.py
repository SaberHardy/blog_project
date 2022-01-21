from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Type your email here'}))

    first_name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'Type your first name'}))

    last_name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'Type your last name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User name'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs=
                                                     {'class': 'form-control', 'placeholder': 'Type your email here'}))

    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                               'placeholder': 'Type your first name'}))

    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                              'placeholder': 'Type your last name'}))

    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                             'placeholder': 'Type your username'}))
    # last_login = forms.CharField(widget=forms.CheckboxInput(attrs=
    #                                                          {'class': 'form-check',
    #                                                           'placeholder': 'Type your email here'}))

    is_superuser = forms.CharField(widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    is_staff = forms.CharField(widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    is_active = forms.CharField(widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    date_joined = forms.CharField(widget=forms.TextInput(attrs=
                                                         {'class': 'form-control',
                                                          'placeholder': 'Date joined'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password', 'is_superuser', 'is_active', 'is_staff', 'date_joined')
