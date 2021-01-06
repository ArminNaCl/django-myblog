from django.urls import path
from myblog import api

urlpatterns = [
    path('post/', api.post_list),
    path('post/<int:pk>/', api.post_detail),
]