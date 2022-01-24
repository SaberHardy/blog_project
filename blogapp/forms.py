from django import forms
from .models import Post, Category, Comment

# This is hard coded
# choices = [('coding', 'coding'), ('sports', 'sports'), ('entertainments', 'entertainments'),]

# Not hard coded
# the return is queryset
choices = Category.objects.all().values_list('name', 'name')

choice_list = []
for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body', 'snippet', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Type your title here'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Type your tag here'}),

            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'type': 'hidden',
                                             'id': 'usernameId'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body', 'snippet')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Type your title here'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Type your tag here'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Type your name here'}),

            'body': forms.Textarea(attrs={'class': 'form-control',
                                          'placeholder': 'Type your comment here'}),
        }
