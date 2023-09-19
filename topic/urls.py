from django.urls import path
from .views import *

urlpatterns = [
    path('', TopicsListView.as_view(), name='topics_list'),
    path('topic/<int:topic_id>/', TopicDetailView.as_view(), name='topic_detail'),
    path('accounts/profile/', ProfileView.as_view(), name='user_profile'),
    path('topic/<int:topic_id>/add_comment/', AddCommentView.as_view(), name='add_comment'),
    path('topic/create/', TopicCreateView.as_view(), name='topic_create'),

    # Add other URL patterns as needed
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
]
