from django.urls import path, include

from .views import PostListAPIView, PostDetailAPIView
from .views import PostListGenericsAPIView, PostDetailGenericsAPIView
from .views import PostListMixins, PostDetailMixins
from .views import PostListGenericAPIView, PostDetailGenericAPIView
from .views import post_list, post_detail, PostViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'viewset-post', PostViewSet)

from .views import CommentView

urlpatterns = [
    path('post/', PostListAPIView.as_view()),
    path('post/<int:pk>/', PostDetailAPIView.as_view()),

    path('generics/post', PostListGenericsAPIView.as_view()),
    path('generics/post/<int:pk>', PostDetailGenericsAPIView.as_view()),
    
    path('mixin/post/', PostListMixins.as_view()),
    path('mixin/post/<int:pk>/', PostDetailMixins.as_view()),

    path('list-create/post/', PostListGenericAPIView.as_view()),
    path('get-update-destroy/post/<int:pk>', PostDetailGenericAPIView.as_view()),

    path('viewset/post', post_list),
    path('viewset/post/<int:pk>', post_detail),

    path('comment/', CommentView.as_view(), name='comment_list')
]