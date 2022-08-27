from django.contrib import admin
from django.urls import path, include
from chatoo.views import  home, signup, dashboard, profile_list, profile
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", home, name="home"),
    path("signup/", signup, name="signup"),
    path("dashboard/", dashboard, name="dashboard"),
    path("profile_list/", profile_list, name="profile_list"),
    path("profile/<int:pk>", profile, name="profile"),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    #path("", include("chatoo.urls")),
]

if	settings.DEBUG:				
    urlpatterns	+=	static(settings.MEDIA_URL,														
    document_root=settings.MEDIA_ROOT)