from django.urls import path
from .views import PostListView, ProfileView, PostDetailView, UserSearch

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('search/', UserSearch.as_view(), name='profile-search'),
]