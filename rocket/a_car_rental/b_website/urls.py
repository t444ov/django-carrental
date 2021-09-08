from django.urls import path
from .views import (
    SuperArticleListView,
    ArticleListView,
    WebsiteArticleListView,
    SuperAboutUsListView,
    AboutUsListView,
    WebsiteAboutUsListView
)
from .views import (
    SuperArticleCreateView,
    SuperAboutUsCreateView
)
from .views import (
    SuperArticleUpdateView,
    SuperAboutUsUpdateView
)
from .views import (
    SuperArticleDeleteView,
    SuperAboutUsDeleteView
)
from .views import (
    SuperArticleDetailView,
    ArticleDetailView,
    WebsiteArticleDetailView,
    SuperAboutUsDetailView
)

urlpatterns = [
    path('attach/article/list/', SuperArticleListView.as_view(), name='article_list'),
    path('overview/article/list/', ArticleListView.as_view(), name='article_list'),
    path('', WebsiteArticleListView.as_view(), name='article_list'),

    path('attach/about_us/list/', SuperAboutUsListView.as_view(), name='about_us_list'),
    path('overview/about_us/list/', AboutUsListView.as_view(), name='about_us_list'),
    path('about_us/list/', WebsiteAboutUsListView.as_view(), name='about_us_list'),

    path('attach/article/create/', SuperArticleCreateView.as_view(), name='article_create'),
    path('attach/about_us/create/', SuperAboutUsCreateView.as_view(), name='about_us_create'),

    path('attach/article/<int:pk>/update/', SuperArticleUpdateView.as_view(), name='article_update'),
    path('attach/about_us/<int:pk>/update/', SuperAboutUsUpdateView.as_view(), name='about_us_update'),

    path('attach/article/<int:pk>/delete/', SuperArticleDeleteView.as_view(), name='article_delete'),
    path('attach/about_us/<int:pk>/delete/', SuperAboutUsDeleteView.as_view(), name='about_us_delete'),

    path('attach/article/<int:pk>/detail/', SuperArticleDetailView.as_view(), name='article_detail'),
    path('overview/article/<int:pk>/detail/', ArticleDetailView.as_view(), name='article_detail'),
    path('article/<int:pk>/detail/', WebsiteArticleDetailView.as_view(), name='article_detail'),
    path('attach/about_us/<int:pk>/detail/', SuperAboutUsDetailView.as_view(), name='about_us_detail'),
]
