from django.urls import path, include
from .views import signup, dashboard, profile_list, profile, home
from django.conf import settings

app_name = "chatoo"

urlpatterns = [
    path("", home, name="home"),
    path('accounts/', include('django.contrib.auth.urls')),
    path("signup/", signup, name="signup"),
    path("dashboard/", dashboard, name="dashboard"),
    path("profile_list/", profile_list, name="profile_list"),
    path("profile/<int:pk>", profile, name="profile"),
]