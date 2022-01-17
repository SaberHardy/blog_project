from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, \
    DetailView, CreateView, UpdateView, DeleteView

from .models import Post
from .forms import PostForm


# Create your views here.
# def home(request):
#     return render(request, 'blogapp/home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'blogapp/home.html'
    # extra_context = {'posts': Post.objects.all()}
    ordering = ['-post_date']


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'blogapp/article_detail.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blogapp/add_post.html'

    # fields = '__all__'


class UpdatePostView(UpdateView):
    model = Post
    form_class = PostForm
    # fields = ['title', 'title_tag', 'body']
    template_name = 'blogapp/edit.html'

    # def form_valid(self, form):
    #     self.object = form.save(commit=False)
    #
    #     # Do any custom stuff here
    #     self.object.save()
    #
    #     return render(self.template_name, self.get_context_data())


class DeletePostView(DeleteView):
    model = Post
    template_name = 'blogapp/delete.html'
    success_url = reverse_lazy('home')
