from django.urls import path
from . import views
from django.urls import path  
from django.urls.conf import include  
from django.conf import settings  
from django.conf.urls.static import static  
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView


urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('new', views.new, name="new"),
    path('account', views.account, name="account"),
    path("search", views.search, name="search"),
    path("forum/post", views.save, name="save"), #api path fetch
    path("forum/close", views.close, name="close"),  #api path fetch
    path('<str:title>', views.thread, name="thread"),  #thread page
    path('forum/<str:username>', views.profile, name="profile"),  #user profile page



 ]

if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)   # settings for image upload