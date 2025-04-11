from django.shortcuts import render

from django.views.generic import ListView, DetailView

from core.models import Post


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    paginate_by = 10
    
    def get_queryset(self):
        return Post.objects.all().order_by('-created_at')
    
class ArticleDetailsViews(DetailView):
    
    model = Post
    template_name = 'article_details.html'