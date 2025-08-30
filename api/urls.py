from django.urls import path
from .views import (
    ApiRootView,
    RegisterView,
    MyTokenObtainPairView,
    PostListCreateView,
    PostDetailView,
    UserProfileView,
    CommentCreateView,
    LikeToggleView,
    FollowToggleView,
    FeedView,
    UserSearchView,
    PostSearchView
)
from rest_framework_simplejwt.views import TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'api'

urlpatterns = [
    path('', ApiRootView.as_view(), name='api-root'),  # <-- API root
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('posts/', PostListCreateView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('posts/<int:post_id>/comment/', CommentCreateView.as_view(), name='comment-create'),
    path('posts/<int:post_id>/like-toggle/', LikeToggleView.as_view(), name='like-toggle'),
    path('users/<int:user_id>/follow-toggle/', FollowToggleView.as_view(), name='follow-toggle'),
    path('feed/', FeedView.as_view(), name='feed'),
    path('search/users/', UserSearchView.as_view(), name='user-search'),
    path('search/posts/', PostSearchView.as_view(), name='post-search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
