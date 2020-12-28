from django.urls import path, re_path
from .views import(
    PostListView
)

urlpatterns = [

    path('blog/' ,PostListView.as_view(),name='blog-view' ),
    
]