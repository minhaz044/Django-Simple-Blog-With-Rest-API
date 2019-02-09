###############Import Section ##############
from rest_framework.generics import (
	RetrieveUpdateAPIView,
	CreateAPIView,
	UpdateAPIView,
	DestroyAPIView,
	RetrieveAPIView,
	ListAPIView
)
from rest_framework.pagination import( 
	PageNumberPagination,
	LimitOffsetPagination
	)
from blogPost.models import Post
from .serializers import (
	PostCreateSerializer,
	PostDetailSerializer,
 	PostListSerializer,
 	PostUpdateSerializer
 )
##############################################

class PostCreateApiView(CreateAPIView):
	queryset=Post.objects.all()
	serializer_class=PostCreateSerializer
	def perform_create(self,serializer):
		serializer.save(author=self.request.user)


class PostDetailApiView(RetrieveAPIView):
	queryset=Post.objects.all()
	serializer_class=PostDetailSerializer

class PostDeleteApiView(DestroyAPIView):
	queryset=Post.objects.all()
	serializer_class=PostDetailSerializer

class PostListApiView(ListAPIView):
	queryset=Post.objects.all()
	serializer_class=PostListSerializer
	Pagination_class=PageNumberPagination

class PostUpdateApiView(RetrieveUpdateAPIView):
	queryset=Post.objects.all()
	serializer_class=PostUpdateSerializer
