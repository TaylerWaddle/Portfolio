from django.urls import path
from .views import Index, ProjectListView, ProjectDetailView, BlogDetailView, BlogListView, AboutTemplateView

urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('projects/', ProjectListView.as_view(), name="projects"),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name="project-details"),
    path('blogs/', BlogListView.as_view(), name="blogs"),
    path('blogs/<int:pk>/', BlogDetailView.as_view(), name="blog-details"),
    path('my-story/', AboutTemplateView.as_view(), name='my-story'),
]

