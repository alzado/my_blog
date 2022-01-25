from unicodedata import name
from django.urls import path, reverse
from . import views


app_name = 'blog_app'

urlpatterns = [
    path('register/', views.UserInfoCreateView.as_view(), name='register'),
    path('login/', views.UserAuthenticationView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('create/', views.PostCreateView.as_view(), name='create'),
    path('update/<int:pk>', views.PostUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.PostDeleteView.as_view(), name='delete'),
    path('comment/<int:pk>', views.CommentCreateView.as_view(), name='comment'),
]
