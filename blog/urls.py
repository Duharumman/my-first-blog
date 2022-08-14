from django.urls import path
from .views import PostList, PostDetails, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetails.as_view(), name='post_detail'),
    path('post/add/', PostCreateView.as_view(), name='post_new'),
    path('update/<int:pk>/', PostUpdateView.as_view(), name='post_edit'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='delete_view'),
]
