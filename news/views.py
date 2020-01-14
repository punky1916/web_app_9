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
        return render(
            request, template_name, {"category_news_list": category_news_list, "category": category}
        )


# class CategoryNewsView(ListView):
#     model = News
#     context_object_name = "category_news_list"
#     template_name = "news/categories.html"

#     # queryset = News.objects.all()

#     def get_queryset(self):
#         print("KWARGS: ", self.kwargs)
#         category_id = self.kwargs["category_id"]
#         category = get_object_or_404(Category, id=category_id)
#         return News.objects.filter(category=category)


class NewsTemplateView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        print(categories)
        category_news_list = {}
        for category in categories:
            # context[category.title] = News.objects.filter(category=category)
            category_news_list[category] = News.objects.filter(category=category)
        context["news_list"] = News.objects.all().order_by("-created_at")[:4]
        context["trending_news"] = News.objects.order_by("-count")
        context["category_news_list"] = category_news_list
        print(context)
        return context
