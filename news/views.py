from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import (
    TemplateView,
    DeleteView,
    UpdateView,
    CreateView,
    ListView,
    DetailView,
)
from news.models import Category, News

# Create your views here.
class CategoryNewsView(View):
    def get(self, request, category_id, *args, **kwargs):
        template_name = "news/categories.html"
        # category = Category.objects.get(pk=category_id)
        category = get_object_or_404(Category, pk=category_id)
        category_news_list = News.objects.filter(category=category)
        return render(request, template_name, {"category_news_list": category_news_list})

    # def post(self, request, *args, **kwargs):
    #     return HttpResponse('POST request!')
