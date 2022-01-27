from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse('article-detail', args=(str(self.id)))
        return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)  # , default="My Awsome Blog!")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # body = models.TextField()
    body = RichTextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default="Uncategorized")
    snippet = models.CharField(max_length=255)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    header_image = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        # return reverse('article-detail', args=(str(self.id)))
        return reverse('home')

    def total_likes(self):
        return self.likes.count()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    bio = models.TextField()

    profile_pic = models.ImageField(null=True, blank=True, upload_to='images/profile')
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    website_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    pinterest_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        # return reverse('article-detail', args=(str(self.id)))
        return reverse('home')


class Comment(models.Model):
    # related name in this case is for indicating in my template and can i use it
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)

    def get_absolute_url(self):
        # return reverse('article-detail', args=(str(self.id)))
        return reverse('home')
