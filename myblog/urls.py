from django.urls import path, re_path
from .views import(
    PostListView,
    SingleView,
    UserView,
    CategoryListView,
    CategoryView,
    like_comment
)

# from django.conf.urls import url
# from django.views.generic.dates import ArchiveIndexView
# from .models import Post

urlpatterns = [

    path('blog/' ,PostListView.as_view(),name='blog-url' ),
    path('blog/categories', CategoryListView.as_view(), name="categories-url"),
    path('blog/categories/<slug:category>',CategoryView.as_view() ,name="category-url"),
    path('blog/<slug:slug>',SingleView.as_view(), name = 'post-url'),
    path('user/<int:author>',UserView.as_view(),name ='user-url'),
    path('blog/like/',like_comment, name ="like_comment"),
    # path('archive/',
    #     ArchiveIndexView.as_view(model=Post, date_field="pub_date"),
    #     name="article_archive"),

]


