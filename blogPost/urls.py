from django.urls import path
from blogPost.views import PostDetailView,PostListView,PostCreateView,PostDeleteView,PostUpdateView


urlpatterns = [
    
    path('',PostListView.as_view(),name='home'),
    path('home/',PostListView.as_view(),name='home'),
    path('detail/<int:id>/',PostDetailView.as_view(),name='postDetail'),
    path('create/',PostCreateView.as_view(),name='postCreate'),
    path('delete/<int:id>/',PostDeleteView.as_view(),name='postDelete'),
    path('update/<int:id>/',PostUpdateView.as_view(),name='postUpdate')

]



