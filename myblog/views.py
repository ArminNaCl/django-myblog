from django.shortcuts import render
from django.views.generic.list import ListView , MultipleObjectMixin
from django.views.generic import DetailView ,FormView
from django.views.generic.edit import ModelFormMixin 



# Create your views here.

from .models import (
    Post,
    Category
)

from .forms import CommentForm

class PostListView(ListView):
    queryset =Post.objects.all()     #filter(draft=False)
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'myblog/index.html'


class UserView(ListView):

    def get_queryset(self):
        author_ = self.kwargs.get("author")
        queryset = Post.objects.filter(author__full_name = author_)
        return queryset
    def get_context_data(self):
        context = super().get_context_data()
        context['author']= self.kwargs.get("author")
        return context

    context_object_name ='posts'
    paginate_by = 3
    template_name = 'myblog/index.html'






class SingleView(ModelFormMixin,DetailView):
    model = Post
    form_class = CommentForm
    template_name = 'myblog/post.html'
    success_url = '#'

    def get_context_data(self,*args,**kwargs):
        context = super(SingleView,self).get_context_data(*args,**kwargs)
        post = context['post']
        context['comments'] = post.comments.all()
        context['settings'] = post.post_setting
        context['form'] = self.get_form()
        return context

    def post (self,request,*args,**kwargs):
        if request.user.is_authenticated:
            form = self.get_form()
            if form.is_valid():
                comment = form.save(commit=False)
                comment.author = request.user
                comment.post = self.get_object()
                comment.save()
                return self.form_valid(form)




class CategoryListView(ListView):
    queryset = Category.objects.all()     
    context_object_name = 'categorys'
    paginate_by = 3
    template_name = 'myblog/categorys.html'


class CategoryView(ListView):
    template_name = 'myblog/single_cat.html'
    context_object_name = 'posts'

    def get_queryset(self):
        category = self.kwargs.get('category')
        queryset = Post.objects.filter(category__slug=category)
        return queryset

    def get_context_data(self,):
        context = super().get_context_data()
        category = self.kwargs.get('category')
        context['name'] = category
        context['sub'] = Category.objects.filter(parent__slug=category)
        return context