from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as Views

urlpatterns = [
    path('',include('blog.urls')),
    path('admin/', admin.site.urls),
    path('accounts/login/', Views.LoginView),
    path('accounts/logout/', Views.LogoutView, name='logout', kwargs={'next_page':'/'}),   
]
