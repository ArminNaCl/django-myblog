from django.shortcuts import render
from django.views.generic.list import ListView , MultipleObjectMixin
from django.views.generic import DetailView ,FormView
from django.views.generic.edit import ModelFormMixin 
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse
from django.contrib.auth import get_user_model 
from django.views.generic import MonthArchiveView , WeekArchiveView
from django.db.models import Q
from django.views.generic import TemplateView

User = get_user_model()


# Create your views here.

from .models import (
    Post,
    Category,
    CommentLike,
    Comment
)

from .forms import CommentForm

class PostListView(ListView):
    queryset =Post.objects.all()     
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'myblog/index.html'
    # def get(self,requist):
    #     query = request.GET



class UserView(ListView):

    def get_queryset(self):
        author_ = self.kwargs.get("author")
        queryset = Post.objects.filter(author__id = author_)
        return queryset
    def get_context_data(self):
        context = super().get_context_data()
        context['author']= User.objects.get(id=self.kwargs.get("author"))
        return context

    context_object_name ='posts'
    paginate_by = 3
    template_name = 'myblog/index.html'


@csrf_exempt
def like_comment(request):
    data = json.loads(request.body)
    user = request.user
    comment_ob = Comment.objects.get(id= data['comment_id'])
    CommentLike.objects.create(author=user,condition = data['condition'],comment= comment_ob)
    return HttpResponse('ok',status=201)


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

class BlogMounthArchive(MonthArchiveView):
    queryset = Post.objects.all()
    date_field = "create_at"
    allow_future = False
    context_object_name = 'posts'
    template_name = 'myblog/month_archive.html'

class BlogWeekArchive(WeekArchiveView):
    queryset = Post.objects.all()
    date_field = "create_at"
    allow_future = False
    context_object_name = 'posts'
    template_name = 'myblog/week_archive.html'  

class BigComments(ListView):
    context_object_name = 'posts'
    template_name = 'myblog/most.html'
    def get_queryset(self):
        queryset =Post.objects.all()
        queryset = sorted(queryset, key=lambda post: post.commentCount,reverse=True)
        return queryset


class SearchView(ListView):
    template_name = 'component/search.html'
    context_object_name = 'posts'
    def get(self, request, *args, **kwargs):
        q = request.GET.get('q', '')
        self.results = Post.objects.filter(
            Q(title__icontains=q)
        )
        self.results =list(set(self.results))
        return super().get(request, *args, **kwargs)
    def get_queryset(self):
        return self.results
