from django.shortcuts import render
from django.views.generic.list import ListView

# Create your views here.

from .models import (
    Post
)

class PostListView(ListView):
    queryset =Post.objects.all()     #filter(draft=False)
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'myblog/index.html'