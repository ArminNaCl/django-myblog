from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .api import (
    # post_detail,
    # post_list,
    # PostListView,
    # PostDetailView,
    # PostListMixin,
    # PostDetailMixin,
    # PostDetailGenerics,
    # PostListGenerics,


    PostViewSet,
    CommentViewSet,
    CategoryViewSet
)

post_list = PostViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
post_detail = PostViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

comment_list = CommentViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
comment_detail = CommentViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
category_list = CategoryViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
category_detail = CategoryViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})



urlpatterns = [
    # path('post/', post_list),
    # path('post/<int:pk>/', post_detail),
    # path('normal/posts/', PostListView.as_view() , name= "post-list-api"),
    # path('normal/posts/<int:pk>', PostDetailView.as_view() , name= "post-detail-api"),
    # path('mixin/posts', PostListMixin.as_view(), name="post-list-mixin"),
    # path('mixin/posts/<int:pk>',PostDetailMixin.as_view(),name= "post-detail-mixin" ),
    # path('generics/posts', PostListGenerics.as_view(), name="post-list-generics"),
    # path('generics/posts/<int:pk>',PostDetailGenerics.as_view(),name= "post-detail-generics" ),


    path('posts/',post_list,name="post-list-api"),
    path('posts/<int:pk>/',post_detail,name="post-detail-api"),
    path('comments/',comment_list,name="comment-list-api"),
    path('comments/<int:pk>/',comment_detail,name = "comment-detail-api"),
    path('categories/',category_list,name="category-list-api"),
    path('categories/<int:pk>/',category_detail,name="category-detail-api"),

]

urlpatterns = format_suffix_patterns(urlpatterns)