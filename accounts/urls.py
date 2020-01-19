from django.urls import path
from accounts.views import UserRegistrationView, activate

# urls
urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="user_register"),
    path("activate/<uidb64>/<token>", activate, name="activate"),
]

