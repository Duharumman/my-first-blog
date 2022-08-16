from django.urls import path, include
from . import views
from .views import PostList, PostDetails, PostCreateView, PostUpdateView, PostDeleteView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('authors', views.AuthorViewSet),
router.register('posts', views.PostViewSet),


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
    path('rest/cbv/<int:pk>', views.CBV_pk.as_view()),

    # 5.1  GET POST From Rest Mixins Framework
    path('rest/mixins', views.Mixins_List.as_view()),

    # 5.2  GET PUT DELETE From Rest Mixins Framework
    path('rest/mixins/<int:pk>', views.Mixins_pk.as_view()),

    # 6.1  GET POST From Rest Generics Framework
    path('rest/generics', views.Generics.as_view()),

    # 6.2  GET PUT DELETE From Rest Generics Framework
    path('rest/generics/<int:pk>', views.Generics_pk.as_view()),

    # 7 ViewSet

    path('rest/viewsets/', include(router.urls))
]
