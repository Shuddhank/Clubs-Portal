"""clubsportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from home import views as home_views
from registration import views as register_views
from django.conf import settings
from django.conf.urls.static import static
from userprofile import views as profile_views
from forum import views as forum_views
from propose_join import views as clubs_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_views.index, name='home'),
    path('propose_join/',include("propose_join.urls")),
    path('registration/',include("registration.urls")),
    path('userprofile/',include("userprofile.urls")),
    path('home/', include("forum.urls")),
    path('administration/', include("administration.urls")),
    path('home/clubs', clubs_views.existingClubList, name='exlist'),
    path('home/proposed-clubs', clubs_views.proposedClubList, name='prlist'),
    path('home/propose-club', clubs_views.proposeClub, name='prclub'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='home/index.html'), name='logout'),
    path('register/',register_views.register, name = 'register'),
    path('home/profile/',profile_views.profile, name = 'profile'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
