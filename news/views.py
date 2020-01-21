from django.shortcuts import render, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.text import slugify
from django.views.generic import (
    TemplateView,
    DeleteView,
    UpdateView,
    CreateView,
    ListView,
    DetailView,
)
from news.models import Category, News
from news.forms import NewsCreateForm

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
        category_news_list = {}
        for category in categories:
            # context[category.title] = News.objects.filter(category=category)
            category_news_list[category] = News.objects.filter(category=category)
        context["news_list"] = News.objects.all().order_by("-created_at")[:4]
        context["trending_news"] = News.objects.order_by("-count")
        context["category_news_list"] = category_news_list
        return context


class NewsDetail(DetailView):
    model = News
    template_name = "news/single_news.html"
    context_object_name = "detail_news"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.count = self.object.count + 1
        self.object.save()
        context["popular_news"] = News.objects.order_by("-count")[:4]
        return context


class NewsCreateView(LoginRequiredMixin, CreateView):
    model = News
    template_name = "news/create.html"
    login_url = "/accounts/login/"
    success_url = "/"
    form_class = NewsCreateForm

    def form_valid(self, form):
        news = form.save(commit=False)
        title = form.cleaned_data["title"]
        slug = slugify(title)
        news.slug = slug
        news.author = self.request.user
        news.save()

        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class NewsUpdateView(LoginRequiredMixin, UpdateView):
    model = News
    template_name = "news/update.html"


class NewsDeleteView(LoginRequiredMixin, DeleteView):
    model = News
    template_name = "news/delete.html"

