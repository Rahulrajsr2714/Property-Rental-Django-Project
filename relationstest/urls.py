from django.urls import path
from . import views
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = [
    # path('login-user',views.login_account, name = 'login_users'),
    path('admin/', admin.site.urls),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)