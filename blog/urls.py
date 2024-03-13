from django.urls import path
from . import views

app_name = 'blog'


urlpatterns = [
    path('', views.BlogListView.as_view(), name='blog_list'),
    path('new/', views.BlogCreateView.as_view(), name='blog_create'),
    path('<int:pk>/', views.BlogDetailView.as_view(), name='blog_detail'),
    path('<int:pk>/update/', views.BlogUpdateView.as_view(), name='blog_update'),
    path('<int:pk>/delete/', views.BlogDeleteView.as_view(), name='blog_delete'),
    path("tag/<str:tag>/", views.BlogTagListView.as_view(), name="blog_tag"),
    path("category/<str:category>/", views.BlogCategoryListView.as_view(), name="blog_cateogry"),
    path('author/<str:username>/', views.AuthorPostsListView.as_view(), name='blog_author'),
    # comment 추가 url 추가
    path(
        "<int:pk>/comment_create/",
        views.CommentCreateView.as_view(),
        name="comment_create",
    ),    
    # comment 삭제 url 추가
    path(
        "<int:pk>/comment_delete/",
        views.CommentDeleteView.as_view(),
        name="comment_delete",
    ),
]