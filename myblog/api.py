from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics


from rest_framework.viewsets import ModelViewSet
from myblog.models import Post,Category,Comment
from myblog.serializers import PostSerializer2,CommentSerializer,CategorySerializer

class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer2
    queryset = Post.objects.all()

class CategoryViewSet(ModelViewSet):
    serializer_class= CategorySerializer
    queryset = Category.objects.all()

class CommentViewSet(ModelViewSet):
    serializer_class= CommentSerializer
    queryset = Comment.objects.all()


class PostListMixin(mixins.CreateModelMixin, mixins.ListModelMixin,generics.GenericAPIView ):
    queryset = Post.objects.all()
    serializer_class = PostSerializer2

    def get(self, request, *args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post (self, request,*args,**kwargs):
        return self.create(request,*args,**kwargs)  

class PostDetailMixin(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset= Post.objects.all()
    serializer_class = PostSerializer2
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class PostListGenerics(generics.ListCreateAPIView):
    queryset= Post.objects.all()
    serializer_class = PostSerializer2

class PostDetailGenerics(generics.RetrieveUpdateDestroyAPIView):
    queryset= Post.objects.all()
    serializer_class = PostSerializer2   

class PostListView(APIView):
    def get(self, request, format=None):
        posts = Post.objects.all()
        serializer = PostSerializer2(posts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        serializer = PostSerializer2(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class PostDetailView(APIView):

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer2(post)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer2(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@csrf_exempt
def post_list(request):
    """
    List all code posts, or create a new post.
    """
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer2(posts, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PostSerializer2(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def post_detail(request, pk):
    """
    Retrieve, update or delete a code post.
    """
    try:
        post = Post.objects.get(pk=pk)
    except post.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PostSerializer2(post)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PostSerializer2(post, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        post.delete()
        return HttpResponse(status=204)