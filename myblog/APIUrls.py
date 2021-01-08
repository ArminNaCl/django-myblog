from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .api import (
    post_detail,
    post_list,
    PostListView,
    PostDetailView,
    PostListMixin,
    PostDetailMixin,
    PostDetailGenerics,
    PostListGenerics,
    PostViewSet
)




urlpatterns = [
    # path('post/', post_list),
    # path('post/<int:pk>/', post_detail),
    path('posts/', PostListView.as_view() , name= "post-list-api"),
    path('posts/<int:pk>', PostDetailView.as_view() , name= "post-detail-api"),
    path('mixin/posts', PostListMixin.as_view(), name="post-list-mixin"),
    path('mixin/posts/<int:pk>',PostDetailMixin.as_view(),name= "post-detail-mixin" ),
    path('generics/posts', PostListGenerics.as_view(), name="post-list-generics"),
    path('generics/posts/<int:pk>',PostDetailGenerics.as_view(),name= "post-detail-generics" ),
    path('viewste/posts',PostViewSet.as_view({'get': 'list'}),name="post-list-viewset")
]

urlpatterns = format_suffix_patterns(urlpatterns)