from pyexpat import model
from statistics import mode
from django import template
from . import models, forms
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

# Create your views here.


class PostListView(ListView):
    context_object_name = 'posts'
    model = models.Post


class PostDetailView(DetailView):
    model = models.Post
    context_object_name = 'post_detail'
    template_name = 'blog_app/post_detail.html'


class PostCreateView(CreateView):
    model = models.Post
    template_name = 'blog_app/post_create.html'
    success_url = reverse_lazy('list')
    fields = ['title', 'post_content']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    context_object_name = 'post'
    model = models.Post
    template_name = 'blog_app/post_update.html'
    fields = ['title', 'post_content']


class PostDeleteView(DeleteView):
    model = models.Post
    success_url = reverse_lazy('list')
    template_name = 'blog_app/post_delete.html'

class CommentCreateView(CreateView):
    context_object_name = 'comment'
    model = models.Comment
    template_name = 'blog_app/comment_create.html'
    fields = ['comment_content']

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

class UserInfoCreateView(CreateView):
    form_class = forms.UserRegisterForm
    success_url = reverse_lazy('list')
    template_name = 'blog_app/user_registration.html'


class UserAuthenticationView(LoginView):
    template_name = 'blog_app/user_login.html'


class UserLogoutView(LogoutView):
    template_name = 'blog_app/user_logout.html'
