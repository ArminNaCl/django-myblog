from rest_framework import serializers
from .models import Post,Category ,Comment
from django.contrib.auth import get_user_model
User =get_user_model()

class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    title = serializers.CharField(max_length=128)
    slug = serializers.SlugField(allow_unicode=False, max_length=50)
    content = serializers.CharField(style={'base_template': 'textarea.html'})
    create_at = serializers.DateTimeField(read_only=True)
    update_at = serializers.DateTimeField(read_only=True)
    publish_time = serializers.DateTimeField(label='Publish at')
    draft = serializers.BooleanField(required=False)
    image = serializers.ImageField(max_length=100)
    category = serializers.PrimaryKeyRelatedField(allow_null=True,queryset=Category.objects.all(),  required=False)
    author = serializers.PrimaryKeyRelatedField(allow_null=True,queryset=User.objects.all(),  required=False)

    # id = IntegerField(label='ID', read_only=True)
    # title = CharField(max_length=128)
    # slug = SlugField(allow_unicode=False, max_length=50, validators=[<UniqueValidator(queryset=Post.objects.all())>])
    # content = CharField(style={'base_template': 'textarea.html'})
    # create_at = DateTimeField(read_only=True)
    # update_at = DateTimeField(read_only=True)
    # publish_time = DateTimeField(label='Publish at')
    # draft = BooleanField(required=False)
    # image = ImageField(max_length=100)
    # category = PrimaryKeyRelatedField(allow_null=True, queryset=Category.objects.all(), required=False)
    # author = PrimaryKeyRelatedField(allow_null=True, queryset=User.objects.all(), required=False)

    def create(self,**validated_data):
        return Post.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.content = validated_data.get('content', instance.content)
        instance.update_at = validated_data.get('update_at', instance.update_at)
        instance.publish_time = validated_data.get('publish_time', instance.publish_time)
        instance.draft = validated_data.get('draft', instance.draft)
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance

class PostSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'