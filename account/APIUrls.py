from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .api import(
    UserViewSet,
)

user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    path('users',user_list,name="user-list-api"),
    path('users/<int:pk>',user_detail,name="user-detail-api"),

]

urlpatterns = format_suffix_patterns(urlpatterns)