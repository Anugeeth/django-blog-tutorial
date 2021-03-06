from django.urls import path
from . import views


urlpatterns = [
    path('',views.PostListView.as_view(), name='blog-home'),
    path('post/new/',views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/',views.PostDetailView.as_view(), name='post-detail'),
    path('post/update/<int:pk>/',views.PostUpdateView.as_view(), name='post-update'),
    path('post/delete/<int:pk>/',views.PostDeleteView.as_view(), name='post-delete'),
    path('about/',views.about, name='blog-about')
]



