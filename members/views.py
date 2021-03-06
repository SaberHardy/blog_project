from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm

from blogapp.views import HomeView
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm, ProfilePageForm
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import DetailView, UpdateView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.views import generic
from blogapp.models import Post, Profile


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/registrations.html'
    success_url = reverse_lazy('login')


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user


class PasswordChangeView(PasswordChangeView):
    # form_class = PasswordChangeForm
    form_class = PasswordChangingForm
    # success_url = reverse_lazy('home')
    success_url = reverse_lazy('password_success')


def password_success(request):
    return render(request, 'registration/password_success.html', {})


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, object_list=None, **kwargs):
        # users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)

        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user'] = page_user

        return context


class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    fields = ['bio', 'profile_pic', 'facebook_url', 'website_url', 'instagram_url', 'pinterest_url']
    success_url = reverse_lazy('home')


class CreateProfilePageView(CreateView):
    model = Profile
    template_name = 'registration/create_user_profile_page.html'
    # fields = "__all__"
    form_class = ProfilePageForm

    # allows project which user to edit.
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
