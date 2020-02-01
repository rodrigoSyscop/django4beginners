from django.shortcuts import render
from django.views.generic import ListView

from .models import Post


class ListPageView(ListView):
    model = Post
    template_name = 'posts/list.html'
    context_object_name = 'all_posts_list'
