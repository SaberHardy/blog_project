from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, \
    DetailView, CreateView, UpdateView, DeleteView

from .models import Post, Category
from .forms import PostForm


# Create your views here.
# def home(request):
#     return render(request, 'blogapp/home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'blogapp/home.html'
    # extra_context = {'posts': Post.objects.all()}
    ordering = ['-post_date']

    def get_context_data(self, *args, object_list=None, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'blogapp/article_detail.html'

    def get_context_data(self, *args, object_list=None, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context


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


class AddCategoryView(CreateView):
    model = Category
    # form_class = PostForm
    template_name = 'blogapp/add_category.html'
    fields = '__all__'


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace("-", ' '))

    return render(request,
                  'blogapp/categories.html',
                  context={'cats': cats.title().replace("-", ' '),
                           'category_posts': category_posts})


def category_list_view(request):
    category_list_posts = Post.objects.all()
    return render(request,
                  'blogapp/category_list.html',
                  context={'category_list_posts': category_list_posts})
