from django.urls import path, re_path
from .views import(
    PostListView,
    SingleView,
    UserView,
    CategoryListView,
    CategoryView,
)

urlpatterns = [

    path('blog/' ,PostListView.as_view(),name='blog-url' ),
    path('blog/categories', CategoryListView.as_view(), name="categories-url"),
    path('blog/categories/<slug:category>',CategoryView.as_view() ,name="category-url"),
    path('blog/<slug:slug>',SingleView.as_view(), name = 'post-url'),
    path('user/<slug:author>',UserView.as_view(),name ='user-url'),
]
