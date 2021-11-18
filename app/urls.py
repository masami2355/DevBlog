
from django.urls import path
from . import views
from .views import BlogDetailView, CreatePostView, IndexView, PostDeleteView, PostEditView

urlpatterns = [
    #path('', views.index, name="home"),
    path('', IndexView.as_view(), name="home"),
    path('post/<int:pk>', BlogDetailView.as_view(), name="detail"), #pkはプライマリーキー　インデックス番号
    path('post/new', views.CreatePostView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', views.PostEditView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    
]