from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import HomeView, ArticleDetailsViews

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>/', ArticleDetailsViews.as_view(), name='article_details')
] 

if settings.DEBUG:urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)