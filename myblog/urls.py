from django.urls import path, re_path
from .views import(
    PostListView,
    SingleView,
    UserView,
    CategoryListView,
    CategoryView,
    like_comment,
    BlogMounthArchive,
    BlogWeekArchive,
    BigComments,
    SearchView,
)

# from django.conf.urls import url
# from django.views.generic.dates import ArchiveIndexView
# from .models import Post

urlpatterns = [

    path('blog/' ,PostListView.as_view(),name='blog-url' ),
    path('blog/categories', CategoryListView.as_view(), name="categories-url"),
    path('blog/categories/<slug:category>',CategoryView.as_view() ,name="category-url"),
    path('blog/as',BigComments.as_view(),name='most_comment'),
    path('blog/search/', SearchView.as_view(), name='search'),
    path('blog/<slug:slug>',SingleView.as_view(), name = 'post-url'),
    path('user/<int:author>',UserView.as_view(),name ='user-url'),
    path('blog/like/',like_comment, name ="like_comment"),
    path('<int:year>/<int:month>/',
         BlogMounthArchive.as_view(month_format='%m'),
         name="archive_month_numeric"),
    path('<int:year>/week/<int:week>/',
         BlogWeekArchive.as_view(),
         name="archive_week"),

]


