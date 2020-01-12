from django.urls import path
from news import views

urlpatterns = [path("<category_id>/", views.CategoryNewsView.as_view(), name="category_news")]
