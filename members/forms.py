from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms

from blogapp.models import Profile


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


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password',
               'placeholder': 'Type your first name'}))

    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password',
               'placeholder': 'Type your first name'}))

    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password',
               'placeholder': 'Type your last name'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')


class ProfilePageForm(forms.ModelForm):
    class Meta:

        model = Profile
        fields = ('bio', 'profile_pic', 'facebook_url', 'website_url', 'instagram_url', 'pinterest_url')

        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control',
                                         'placeholder': 'Type your title here'}),
            # 'profile_pic': forms.TextInput(attrs={'class': 'form-control',
            #                                     'placeholder': 'Type your tag here'}),

            'facebook_url': forms.TextInput(attrs={'class': 'form-control'}),
            'website_url': forms.TextInput(attrs={'class': 'form-control'}),
            'instagram_url': forms.TextInput(attrs={'class': 'form-control'}),
            'pinterest_url': forms.TextInput(attrs={'class': 'form-control'}),
        }
