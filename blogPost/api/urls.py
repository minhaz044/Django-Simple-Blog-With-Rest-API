from django.urls import path
from blogPost.api.views import (
        PostCreateApiView,
		PostUpdateApiView,
		PostDeleteApiView,
		PostDetailApiView,
		PostListApiView
 	)


urlpatterns = [
    
    path('',PostListApiView.as_view(),name='apiHome'),
    path('home/',PostListApiView.as_view(),name='apiHome'),
    path('detail/<int:pk>/',PostDetailApiView.as_view(),name='postApiDetail'),
    path('create/',PostCreateApiView.as_view(),name='postApiCreate'),
    path('delete/<int:pk>/',PostDeleteApiView.as_view(),name='postApiDelete'),
    path('update/<int:pk>/',PostUpdateApiView.as_view(),name='postApiUpdate')

]



