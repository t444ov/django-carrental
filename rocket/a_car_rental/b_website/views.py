from .models import Article, AboutUs
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView


class SuperArticleListView(ListView):
    model = Article
    template_name = 'b_website/list_view/super_article_list.html'


class ArticleListView(ListView):
    model = Article
    template_name = 'b_website/list_view/article_list.html'


class WebsiteArticleListView(ListView):
    model = Article
    template_name = 'b_website/list_view/website_article_list.html'


class SuperArticleCreateView(CreateView):
    model = Article
    fields = '__all__'
    template_name = 'b_website/create_view/super_article_create.html'
    success_url = '/attach/article/list/'


class SuperArticleUpdateView(UpdateView):
    model = Article
    fields = '__all__'
    template_name = 'b_website/update_view/super_article_update.html'
    success_url = '/attach/article/list/'


class SuperArticleDeleteView(DeleteView):
    model = Article
    template_name = 'b_website/delete_view/super_article_confirm_delete.html'
    success_url = '/attach/article/list/'


class SuperArticleDetailView(DetailView):
    model = Article
    template_name = 'b_website/detail_view/super_article_detail.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'b_website/detail_view/article_detail.html'


class WebsiteArticleDetailView(DetailView):
    model = Article
    template_name = 'b_website/detail_view/website_article_detail.html'


class SuperAboutUsListView(ListView):
    model = AboutUs
    template_name = 'b_website/list_view/super_about_us_list.html'


class AboutUsListView(ListView):
    model = AboutUs
    template_name = 'b_website/list_view/about_us_list.html'


class WebsiteAboutUsListView(ListView):
    model = AboutUs
    template_name = 'b_website/list_view/website_about_us_list.html'


class SuperAboutUsCreateView(CreateView):
    model = AboutUs
    fields = '__all__'
    template_name = 'b_website/create_view/super_about_us_create.html'
    success_url = '/attach/about_us/list/'


class SuperAboutUsUpdateView(UpdateView):
    model = AboutUs
    fields = '__all__'
    template_name = 'b_website/update_view/super_about_us_update.html'
    success_url = '/attach/about_us/list/'


class SuperAboutUsDeleteView(DeleteView):
    model = AboutUs
    template_name = 'b_website/delete_view/super_about_us_confirm_delete.html'
    success_url = '/attach/about_us/list/'


class SuperAboutUsDetailView(DetailView):
    model = AboutUs
    template_name = 'b_website/detail_view/super_about_us_detail.html'
