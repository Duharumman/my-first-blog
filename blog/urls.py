from django.urls import path

from . import views
from .views import PostList, PostDetails, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetails.as_view(), name='post_detail'),
    path('post/add/', PostCreateView.as_view(), name='post_new'),
    path('update/<int:pk>/', PostUpdateView.as_view(), name='post_edit'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='delete_view'),

    # # start Django rest-framework
    # 1 json response no model
    path('django/', views.no_rest_no_model),

    # 2 json response from model
    path('django/model', views.no_model_from_model),

    # 3.1 GET POST FROM  rest framework  function based views
    path('rest/fbs', views.FBV_List),

    # 3.2 GET PUT DELETE FROM  rest framework  function based views
    path('rest/fbs/<int:pk>', views.FBV_pk),


    # 4.1 GET POST From Rest  Framework  Class  based views
    path('rest/cbv', views.CBV_List.as_view()),

    # 4.2 GET PUT DELETE FROM  Rest  Framework  Class  based views
    path('rest/cbv/<int:pk>', views.CBV_pk.as_view())

]
