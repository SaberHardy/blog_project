from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
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

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        context['cat_menu'] = cat_menu
        context['total_likes'] = total_likes
        context['liked'] = liked
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


def like_unlike_post(request, pk):
    # this post_id is the name of post was liked
    id_liked = request.POST.get('post_id')
    post_liked = get_object_or_404(Post, id=id_liked)
    liked = False
    user_id = request.user.id
    if post_liked.likes.filter(id=user_id).exists():
        post_liked.likes.remove(request.user)
        liked = False
    else:
        post_liked.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))
